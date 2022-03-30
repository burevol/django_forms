from django.db import models


# Create your models here.

class Category(models.Model):
    cat = models.CharField(max_length=255)

    def __str__(self):
        return self.cat


class Questions(models.Model):
    text = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text