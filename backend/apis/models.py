from django.db import models


# Create your models here.

# manufactor model
class NameBasedModel(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        abstract = True        


# manufactor model
class Manufactor(NameBasedModel):
    pass

# Manufactor Model model
class ManufactorModel(NameBasedModel):
    pass

# Showroom model
class Showroom(NameBasedModel):
    logo = models.ImageField(upload_to='all_image',blank= 'True')

#User model
class User(NameBasedModel):
    email = models.CharField(max_length = 100)   

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