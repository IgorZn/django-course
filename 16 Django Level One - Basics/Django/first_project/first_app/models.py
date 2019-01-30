from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

## Exercise
class My_Roles(models.Model):
    user_role = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.user_role

class Users(models.Model):
    role = models.ForeignKey(My_Roles)
    first_name = models.CharField(max_length=264, unique=False)
    last_name = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name