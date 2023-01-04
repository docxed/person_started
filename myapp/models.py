from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname