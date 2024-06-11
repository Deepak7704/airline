from django.db import models

# Create your models here.
class Aiport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}({self.code})"
    

class Flights(models.Model):
    origin=models.ForeignKey(Aiport,on_delete=models.CASCADE,related_name="departure")
    destination=models.ForeignKey(Aiport,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()


    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"
    
    def is_valid(self):
        return self.origin != self.destination or self.duration>0

class Passenger(models.Model):
    firstname=models.CharField(max_length=64)
    lastname=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flights,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"