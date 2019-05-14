from django.db import models

transmission_choices = [
("Manual","Manual"),
("Automatic","Automatic")
]

# status_choice = [
#     ("sold","sold"),
#     ("In stock","In stock")
# ]

# Create your models here.
class Manufactor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ManufactorModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name  


class Showroom(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.CharField(max_length = 3550)

    def __str__(self):
        return self.name           


class Car(models.Model):
    image = models.ImageField(upload_to='all_image',blank= 'True')
    tagline = models.CharField(max_length = 100)
    mileage = models.CharField(max_length = 50)
    year = models.IntegerField(null=True)
    model = models.CharField(max_length=50)
    status = models.BooleanField(null=True)
    transmission = models.CharField(max_length = 50,choices = transmission_choices)
    price = models.IntegerField(null=True)
    horse_power = models.IntegerField(null=True)
    propellant = models.CharField(max_length=100)
    showroom = models.ForeignKey(Showroom , related_name = "car_showroom",on_delete=models.CASCADE)
    manufactor = models.ForeignKey(Manufactor , on_delete=models.CASCADE)

    def __str__(self):
        return self.name 


class User(models.Model):
    name =  models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)   

    def __str__(self):
        return self.name  