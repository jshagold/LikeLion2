from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    attendent = models.BooleanField()

    def __str__(self):
        return self.name