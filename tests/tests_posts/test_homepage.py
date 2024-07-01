"""Unit tests for Post model"""
import json
from http import HTTPStatus

from django.test import TestCase
from model_bakery import baker

from posts.models import Post

# Create your tests here.

HOMEPAGE_URL = "http://127.0.0.1:8000/posts/"
POSTS_BASE_URL = "http://127.0.0.1:8000/posts/"


class TestHomePage(TestCase):
    """test home page"""

    def setUp(self) -> None:
        self.post1 = Post.objects.create(
            title="Homepage1", body="This is the homepage1 content"
        )
        self.post2 = Post.objects.create(
            title="Homepage2", body="This is the homepage2 content"
        )

    def test_homepage_returns_correct_response(self):
        """test if homepage has elements"""
        response = self.client.get(HOMEPAGE_URL)
        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        """test posts created"""
        response = self.client.get(HOMEPAGE_URL)

        # self.assertContains(response, "Django")
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)
