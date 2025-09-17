from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('jacket', 'Jacket'),
        ('shorts', 'Shorts'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
        ('socks', 'Socks'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name