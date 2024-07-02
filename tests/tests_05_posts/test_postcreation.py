from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from posts.forms import PostCreationForm
from posts.models import Post

User = get_user_model()


class PostCreationTest(TestCase):
    def setUp(self):
        self.url = reverse("create_post")
        self.template_name = "posts/createpost.html"
        self.form_class = PostCreationForm
        self.title = "Sample title"
        self.body = "Sample body for the sample text"

        User.objects.create_user(
            username="admin", email="admin@test.com", password="password2024"
        )

    def test_post_creation_page_exists(self):
        self.client.login(username="admin", password="password2024")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)

        form = response.context.get("form", None)

        self.assertIsInstance(form, self.form_class)

    def test_post_creation_form_creates_post(self):
        post_request = HttpRequest()

        post_request.user = baker.make(User)

        post_data = {"title": self.title, "body": self.body}

        post_request.POST = post_data

        form = self.form_class(post_request.POST)

        self.assertTrue(form.is_valid())

        post_obj = form.save(commit=False)
        self.assertIsInstance(post_obj, Post)

        post_obj.author = post_request.user

        post_obj.save()

        self.assertEqual(Post.objects.count(), 1)

    def test_post_creation_requires_login(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response, expected_url="/accounts/login/?next=/posts/create_post/"
        )
