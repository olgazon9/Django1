from django.db import models

class Product(models.Model):
    category_choices = (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Home and Garden', 'Home and Garden'),
        ('Toys', 'Toys'),
        ('Sports and Outdoors', 'Sports and Outdoors'),
        # Add more categories as needed
    )

    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=category_choices)

    def __str__(self):
        return self.description

# Create your models here.
