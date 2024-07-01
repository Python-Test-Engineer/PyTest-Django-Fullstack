from django.test import TestCase
from django.urls import reverse
from ecommerce.factories import RestaurantFactory
from ecommerce.models import Restaurant
from http import HTTPStatus

HOMEPAGE_URL = "http://127.0.0.1:8000/ecommerce/"
NEW = "http://127.0.0.1:8000/ecommerce/restaurants/new/"
POSTS_BASE_URL = "http://127.0.0.1:8000/posts/"


class RestaurantViewsTest(TestCase):

    def test_homepage_returns_correct_response(self):
        """test if homepage has elements"""
        # response = self.client.get(HOMEPAGE_URL)
        response = self.client.get(reverse("restaurant_list"))
        self.assertTemplateUsed(response, "ecommerce/restaurant_list.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_restaurant_create_view(self):
        response = self.client.get(NEW)

        with self.subTest("GET request returns 200"):
            self.assertEqual(response.status_code, 200)

        with self.subTest("GET request uses correct template"):
            self.assertTemplateUsed(response, "ecommerce/restaurant_form.html")

        with self.subTest("POST request creates new restaurant"):
            data = {
                "name": "New Restaurant",
                "address_first_line": "123 New Street",
                "phone_number": "987-654-3210",
                "zip_code": "12345",
            }
            self.client.post(reverse("restaurant_create"), data)

            last_restaurant = Restaurant.objects.last()
            self.assertEqual(last_restaurant.name, "New Restaurant")

    # def test_restaurant_update_view(self):
    #     restaurant = RestaurantFactory()

    #     with self.subTest("GET request returns 200"):
    #         response = self.client.get(reverse("restaurant_edit", args=[restaurant.pk]))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertTemplateUsed(response, "restaurant_form.html")

    #     with self.subTest("POST request updates restaurant"):
    #         data = {
    #             "name": "Updated Restaurant",
    #             "address": "456 Updated Street",
    #             "phone_number": "111-222-3333",
    #         }
    #         response = self.client.post(
    #             reverse("restaurant_edit", args=[restaurant.pk]), data
    #         )

    #     with self.subTest("POST request updates restaurant"):
    #         self.assertEqual(response.status_code, 200)

    # def test_restaurant_delete_view(self):
    #     restaurant = RestaurantFactory()

    #     with self.subTest("GET request returns 200"):
    #         response = self.client.get(
    #             reverse("restaurant_delete", args=[restaurant.pk])
    #         )
    #         self.assertEqual(response.status_code, 200)

    #     with self.subTest("GET request uses correct template"):
    #         response = self.client.get(
    #             reverse("restaurant_delete", args=[restaurant.pk])
    #         )
    #         self.assertTemplateUsed(response, "restaurant_confirm_delete.html")

    #     with self.subTest("POST request deletes restaurant"):
    #         self.client.post(reverse("restaurant_delete", args=[restaurant.pk]))

    #         self.assertFalse(Restaurant.objects.filter(pk=restaurant.pk).exists())
