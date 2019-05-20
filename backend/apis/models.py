from django.db import models

# Create your models here.


# manufactor model
class Manufactor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Manufactor Model model
class ManufactorModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

# Showroom model
class Showroom(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='all_image',blank= 'True')

    def __str__(self):
        return self.name          

#User model
class User(models.Model):
    name =  models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)   

    def __str__(self):
        return self.name          

# Car model


transmission_choices = [
    ("Manual","Manual"),
    ("Automatic","Automatic")
]

status_choices = [
    ("sold","sold"),
    ("In stock","In stock")
]

class Car(models.Model):
    image = models.ImageField(upload_to='all_image',blank= 'True')
    tagline = models.CharField(max_length = 100)
    mileage = models.CharField(max_length = 50)
    year = models.IntegerField(null=True)
    model = models.CharField(max_length=50)
    status = models.CharField(max_length = 50,choices = status_choices)
    transmission = models.CharField(max_length = 50,choices = transmission_choices)
    price = models.IntegerField(null=True)
    horse_power = models.IntegerField(null=True)
    propellant = models.CharField(max_length=100)

    showroom = models.ForeignKey(Showroom , related_name = "car_showroom",on_delete=models.CASCADE)
    manufactor = models.ForeignKey(Manufactor , on_delete=models.CASCADE)

    def __str__(self):
        return self.name   