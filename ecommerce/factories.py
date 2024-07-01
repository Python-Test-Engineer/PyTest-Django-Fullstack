import factory
from faker import Faker
from .models import Restaurant, Ingredient, Dish
from decimal import Decimal
from factory.django import DjangoModelFactory

fake = Faker()


class RestaurantFactory(DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Sequence(lambda n: f"Restaurant {n}")
    address_first_line = fake.address()
    phone_number = fake.phone_number()


class DishFactory(DjangoModelFactory):
    class Meta:
        model = Dish

    name = factory.Sequence(lambda n: f"Dish {n}")
    price = Decimal(fake.random_number(2))
    restaurant = Restaurant


class IngredientFactory(DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = factory.Sequence(lambda n: f"Ingredient {n}")
    unit_price = Decimal(fake.random_number(2))
