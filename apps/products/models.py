from django.db import models

from apps.products.services import normalize_text


class Product(models.Model):
    class CurrencyChoices(models.TextChoices):
        UZS = 'UZS'
        USD = 'USD'
        EUR = 'EUR'

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    brand_slug = models.SlugField(max_length=100, unique=True)
    disc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='product_image/%Y/%m/%d')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    currency = models.CharField(max_length=10, choices=CurrencyChoices.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brand}: {self.title}'

    def save(self, *args, **kwargs):
        normalize_text(self)

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('brand', 'title', 'size')
