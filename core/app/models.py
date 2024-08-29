from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Color(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='media/category_img')

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Collaboration(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Shoes(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    collaboration = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    material = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    picture_side = models.ImageField(upload_to='media/shoes_side_img')
    picture_forward = models.ImageField(upload_to='media/shoes_forward_img')
    picture_back = models.ImageField(upload_to='media/shoes_back_img')
    picture_sole = models.ImageField(upload_to='media/shoes_sole_img')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Shoes, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} {self.product.name}"
