from django.db import models

# Create your models here.
class Category(models.Model) :
    categorys = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.categorys



class Restaurant(models.Model) :
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 20, unique = True)
    num = models.CharField(max_length = 15, default="000-0000-0000")
    locate = models.CharField(max_length = 10, default="")
    address = models.TextField(default="")
    rate = models.FloatField()
    info = models.TextField()

    def __str__(self):
        return self.name