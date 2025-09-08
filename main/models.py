from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tshirt', 'T-Shirt'),
        ('jacket', 'Jacket'),
        ('shorts', 'Shorts')
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

