from django.db import models

# Create your models here.
class Members(models.Model) :
    name = models.CharField(max_length = 20)
    age = models.CharField(max_length = 10)
    birthday = models.DateField()
    nationality = models.CharField(max_length = 20)
    position = models.TextField()

    def __str__(self):
        return self.name


