from django.db import models

# Create your models here.

TRANSMISSION = (
    ('AT', 'AUTOMATIC'),
    ('M', 'MANUAL'),
)
VERSION_BODY = (
    ('KOM', 'KOMBI'),
    ('SED', 'SEDAN'),
    ('HAT', 'HATCHBACK'),
    ('SUV', 'SUV')
)

TYPE_OF_BIKE = (
    ('S', 'SPORT'),
    ('N', 'NAKED'),
    ('C', 'CHOPPER'),
    ('E', 'ENDURO')
)

class Manufacturer(models.Model):
    name = models.CharField(max_length=200, name="name_manufacturer")
    country = models.CharField(max_length=200, name="country_manufacturer")

class VehicleAbstract(models.Model):
    color = models.CharField(max_length=200)
    engine_capacity = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    acceleration = models.DecimalField(decimal_places=2, max_digits=99)
    vin = models.CharField(max_length=150)
    register_number = models.CharField(max_length=50)
    vmax = models.IntegerField()
    class Meta:
        abstract=True

class Parking(models.Model):
    address = models.CharField(max_length=200)
    level = models.IntegerField()
    number_of_place = models.CharField(max_length=250)

class Car(VehicleAbstract):
    transmission = models.CharField(choices=TRANSMISSION, max_length=200)
    body_version = models.CharField(choices=VERSION_BODY, max_length=200)
    parking = models.OneToOneField(Parking, on_delete=models.CASCADE)

class Motorcycle(VehicleAbstract):
    type_of_bike = models.CharField(choices=TYPE_OF_BIKE, max_length=250)
    parking = models.OneToOneField(Parking, on_delete=models.CASCADE)

class Owner(models.Model):
    name=models.CharField(max_length=250)
    surname=models.CharField(max_length=250)
    cars = models.ManyToManyField(Car)
    motorcycles = models.ManyToManyField(Motorcycle)

    def __str__(self):
        return ("{name} {surname}").format(name=self.name, surname=self.surname)

    def show_who_have_many_cars(self):
        best_buyer_cars = self.objects.all().order_by('cars')[0]
        return best_buyer_cars

class OwnerSortedByName(Owner):
    class Meta:
        proxy = True
        ordering = ['name']