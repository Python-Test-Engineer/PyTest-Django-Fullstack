"""Unit tests for Post model"""
import json
import random
from http import HTTPStatus

from django.test import TestCase
from playwright.sync_api import Page, expect, sync_playwright

from filemanager.models import UserFile

DOCS_URL = "https://playwright.dev/python/docs/intro"
# Create your tests here.

HOMEPAGE_URL = "http://127.0.0.1:8000/filemanager/"


class TestHomePage(TestCase):
    """test home page"""

    def test_ut_homepage_returns_correct_response(self):
        """test if homepage has elements"""
        response = self.client.get(HOMEPAGE_URL)
        self.assertTemplateUsed(response, "filemanager/upload_file.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_ut_homepage_returns_correct_response(self):
        """test if homepage has elements"""
        response = self.client.get(HOMEPAGE_URL)
        self.assertTemplateUsed(response, "filemanager/upload_file.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # def test_pl(page: Page):
    #     playwright = sync_playwright().start()

    #     browser = playwright.chromium.launch()
    #     page = browser.new_page()
    #     page.goto(HOMEPAGE_URL)

    #     random_number = random.randint(10_000, 90_000)
    #     print(random_number)
    #     page.screenshot(
    #         path=f"filemanager/tests/screenshots/example-{random_number}.png"
    #     )
    #     browser.close()

    #     playwright.stop()
