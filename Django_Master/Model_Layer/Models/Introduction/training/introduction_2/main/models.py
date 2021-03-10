from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nazwa kategorii")

class ProductPhotos(models.Model):
    name = models.CharField(max_length=250, verbose_name="Tekst alternatywny dla zdjęcia")
    avatar = models.BooleanField(default=False, verbose_name="Czy jest avatarem ?")
    photo = models.ImageField(verbose_name="Zdjęcie")


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nazwa produktu")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria do której należy produkt")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Cena produktu")
    description = models.TextField(verbose_name="Opis produktu")
    date_release = models.DateField(verbose_name="Data produkcji")
    photos = models.ManyToManyField(ProductPhotos, verbose_name="Zdjęcia produktu")
    count_in_warehouse = models.IntegerField(verbose_name="Ilość dostępna na magazynie")

    def __str__(self):
        return self.name

    def show_via_release(self):
        all_objects = self.objects.all().order_by('-date_release')
        return all_objects

class ProductViaPrice(Product):
    class Meta:
        proxy = True
        ordering = ['-price']

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Właściciel koszyka na zakupy")
    products = models.ManyToManyField(Product, verbose_name="Produkty w koszyku na zakupy")

class PromotionCode(models.Model):
    code = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    percent_of_promotion = models.IntegerField()
    start_life = models.DateTimeField()
    end_of_life = models.DateTimeField()

class UsedPromotionCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.ForeignKey(PromotionCode, on_delete=models.CASCADE)
    date_use = models.DateTimeField(auto_now_add=True)

class MailingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
