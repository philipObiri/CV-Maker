from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=500)
    previous_work = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name}'s Profile"
