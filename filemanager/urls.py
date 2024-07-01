from django.urls import path

from . import views

urlpatterns = [
    path("", views.UploadFile.as_view()),
    path("upload/", views.UploadFile.as_view()),
    path("list/", views.ListFiles.as_view()),
]
