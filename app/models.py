from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    editor_note = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)

    def __str__(self):
        return self.name
