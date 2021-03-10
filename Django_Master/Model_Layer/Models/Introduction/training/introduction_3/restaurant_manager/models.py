from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYP_RESTAURACJI = (
    ("KEBAB", "KEBAB"),
    ("PIZZA", "PIZZA"),
    ("MAKARON", "MAKARON")
)
HOT_LEVEL = (
    ('0', 'ŁAGODNY'),
    ('1', 'DELIKATNIE OSTRY'),
    ('2', 'ŚREDNIO OSTRY'),
    ('3', 'OSTRY'),
    ('4', 'BARDZO OSTRY'),
    ('5', 'ŚLUZUWKO-WYPALATOR')
)

class Location(models.Model):
    street = models.CharField(max_length=200, verbose_name="Ulica")
    town = models.CharField(max_length=200, verbose_name="Miasto")
    postal_code = models.CharField(max_length=200, verbose_name="Kod Pocztowy")

class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa restauracji", unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    count_max_clients = models.IntegerField(verbose_name="Maksymalna liczba klientów w jednym czasie")
    type_of_restaurant = models.CharField(max_length=200, choices=TYP_RESTAURACJI)

    def show_max_size_restaurants(self):
        return self.objects.all().order_by('count_max_clients')

class DishInMenuAbstract(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa potrawy")
    hot_level = models.CharField(max_length=200, choices=HOT_LEVEL, verbose_name="Poziom ostrości potrawy")
    description = models.TextField()
    photo = models.ImageField()
    class Meta:
        abstract = True

class DishInMenu(DishInMenuAbstract):
    price = models.DecimalField(max_digits=100, decimal_places=2)

class MenuCard(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    dishes_in_card = models.ManyToManyField(DishInMenu)

class RestaurantViaName(Restaurant):
    class Meta:
        proxy=True
        ordering = ['name']