from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# A table to store user login data
from django.contrib.auth.models import User
from django.db import models

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=255)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
# Product Category
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255) 
    def __str__(self):
        return self.name
    
# Product table
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image=models.ImageField(default='/static/images/jeans.jpg',upload_to='products_img')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
# Order table
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

# Order items
class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

# Product reviews
class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateField()

# Payments
class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    def __str__(self):
        return self.payment_id

# Cart
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)