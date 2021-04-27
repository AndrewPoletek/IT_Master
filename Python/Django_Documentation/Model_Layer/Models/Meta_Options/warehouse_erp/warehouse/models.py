from django.db import models
from django.contrib.auth.models import User, Group

class ProductCard(models.Model):
    name = models.CharField(max_length=250, unique=True)
    weight = models.DecimalField(decimal_places=4, max_digits=1000000)
    color = models.CharField(max_length=150)
    producent = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=250)
    barcode = models.CharField(max_length=150)
    sugested_margin = models.IntegerField()
    sugested_price = models.DecimalField(decimal_places=2, max_digits=1000000)
    #Size in centemeters
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()

class Warehouse(models.Model):
    name = models.CharField(max_length=250, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group_owners = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

class ProductsInWarehouse(models.Model):
    wh = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    type_product = models.ForeignKey(ProductCard, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=1000000)

TYPE_MOVING_DOCS = (
    ('PZ', 'PRZYJĘCIE ZEWNĘTRZNE'),
    ('PW', 'PRZYJĘCIE WEWNĘTRZNE'),
    ('ZW', 'ZWROT WEWNĘTRZNY'),
    ('MM', 'PRZESUNIĘCIE MIĘDZYMAGAZYNOWE'),
    ('WZ', 'WYDANIE ZEWNĘTRZNE'),
    ('RW', 'ROZCHÓD WEWNĘTRZNY'),
)

class WarehouseMovingDocs(models.Model):
    from_wh = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="from_wh", null=True)
    to_wh = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="to_wh", null=True)
    type_doc = models.CharField(choices=TYPE_MOVING_DOCS, max_length=150)