"""Quick check of playwright functionality working..."""
import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright


class MyViewTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_pl_login(self):
        page = self.browser.new_page()
        page.goto(f"{self.live_server_url}/admin/")
        page.wait_for_selector("text=Django administration")
        page.fill("[name=username]", "admin@test.com")
        page.fill("[name=password]", "password")
        print("PLAYWRIGHT ---> test_pl_login")
        page.click("text=Log in")
        assert len(page.eval_on_selector(".errornote", "el => el.innerText")) > 0
        page.close()
