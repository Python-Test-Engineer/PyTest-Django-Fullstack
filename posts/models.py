from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()
# Create your models here.

"""
    class Post
        -id:int
        -title:varchar
        -body:text
        -created_at:datetime
        -modified_at:datetime
"""


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.pk})
