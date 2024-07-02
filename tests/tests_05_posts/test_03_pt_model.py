"""Unit tests for Post model"""
import json
from http import HTTPStatus

from django.test import TestCase
from model_bakery import baker

from posts.models import Post

# Create your tests here.

HOMEPAGE_URL = "http://127.0.0.1:8000/posts/"
POSTS_BASE_URL = "http://127.0.0.1:8000/posts/"


class TestPostModel(TestCase):
    """Post model test"""

    def test_post_model_exists(self):
        """test Posts model exists"""
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_str_rep_of_objects(self):
        """test __str__"""
        post = Post.objects.create(title="First Post", body="First Post body")

        self.assertEqual(post.title, "First Post")
