from django.db import models

# Create your models here.
DroneModelChoices = [
    ("Lightweight", "Lightweight"),
    ("Middleweight", "Middleweight"),
    ("Cruiserweight", "Cruiserweight"),
    ("Heavyweight", "Heavyweight")
]
DroneState = [
    ("IDLE", "IDLE"),
    ("LOADING", "LOADING"),
    ("LOADED", "LOADED"),
    ("DELIVERING", "DELIVERING"),
    ("DELIVERED", "DELIVERED"),
    ("RETURNING", "RETURNING")
]


class Medication(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    image = models.ImageField()


class Drone(models.Model):
    serialNumber = models.CharField(name="serialNumber", max_length=100)
    model = models.CharField(choices=DroneModelChoices, max_length=50)
    weightLimit = models.IntegerField()
    batteryCapacity = models.IntegerField()
    state = models.CharField(choices=DroneState, max_length=50)



class Command(models.Model):
    drone = models.ForeignKey(Drone,on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication,on_delete=models.CASCADE)

class Transaction(models.Model):
    transactionId = models.CharField(max_length=150)
    achieved = models.BooleanField(default=False)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
