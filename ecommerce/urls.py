from django.urls import path
from . import views

# app_name = "ecommerce"
urlpatterns = [
    path("", views.restaurant_list, name="restaurant_list"),
    path("restaurants/new/", views.restaurant_create, name="restaurant_create"),
    path("restaurants/<int:pk>/edit/", views.restaurant_update, name="restaurant_edit"),
    path(
        "restaurants/<int:pk>/delete/",
        views.restaurant_delete,
        name="restaurant_delete",
    ),
]
