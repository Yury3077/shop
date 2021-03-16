from django.db import models
from django.contrib.auth.models import User


class Consumer(User):
    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=15, default="")
    address = models.TextField(default="")
    class Meta:
        verbose_name = "Consumer"
        verbose_name_plural = "Consumers"

    def __str__(self):
        return self.name

    
class Category(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="img", null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    article = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="fabric")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=300, default="")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return "%s (%s)" % (self.name, self.category)


class Order(models.Model):
    
    STATUS = (
        ("new", "new order"),
        ("done", "finished order")
    )
    
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default="new", choices=STATUS)
    receiver = models.TextField(max_length=300, default="")
    adress = models.TextField(max_length=300, default="")


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    ammount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "OrderProduct"
        verbose_name_plural = "OrderProducts"