from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    post_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
