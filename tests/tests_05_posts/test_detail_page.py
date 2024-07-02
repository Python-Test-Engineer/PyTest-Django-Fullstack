"""Unit tests for Post model"""
import json
from http import HTTPStatus

from django.test import TestCase
from model_bakery import baker

from posts.models import Post

# Create your tests here.

HOMEPAGE_URL = "http://127.0.0.1:8000/posts/"
POSTS_BASE_URL = "http://127.0.0.1:8000/posts/"


class TestDetailPage(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(
            title="Detail Homepage", body="This is the homepage detail"
        )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
