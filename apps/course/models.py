from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):

    name = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True)

    def __str__(self) -> str:
        return self.name

