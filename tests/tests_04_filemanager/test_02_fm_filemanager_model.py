"""Unit tests for Post model"""
import json
from http import HTTPStatus

from django.test import TestCase
from model_bakery import baker

from filemanager.models import UserFile

HOMEPAGE_URL = "http://127.0.0.1:8000/posts/"
POSTS_BASE_URL = "http://127.0.0.1:8000/posts/"


class TestUserFileModel(TestCase):
    """UserFile model test"""

    def test_ut_userfile_model_exists(self):
        """test userfile model exists"""
        files = UserFile.objects.count()
        print(f"Number of files: {files}")

        self.assertEqual(files, 0)

    def test_ut_str_rep_of_objects(self):
        """test __str__"""
        file = UserFile.objects.create(filename="test.pdf")

        self.assertEqual(file.filename, "test.pdf")
