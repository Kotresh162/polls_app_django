from random import choices
from tkinter import CASCADE
from tkinter.messagebox import CANCEL
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from traitlets import default
# Create your models here.
class User(AbstractUser):
    pass
    
class Product(models.Model):
     name = models.CharField(max_length=200)
     description = models.TextField()
     price = models.DecimalField(max_digits=10,decimal_places=2)
     stock = models.PositiveIntegerField()
     image = models.ImageField(upload_to="products/",blank=True,null=True)
     
     @property
     def in_stock(self):
         return self.stock > 0
     
     def __str__(self):
         return self.name
     
     
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "pendig"
        CONFIRMED = "confirmed"
        CANCELLED = "cancelled"
        
        
    ordered_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
        )
    Products = models.ManyToManyField(Product,through="OrderItem",related_name="orders")
    def __str__(self):
        return f"Order {self.ordered_id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qauntity = models.PositiveIntegerField()
    
    @property
    def item_subtotal(self):
        return self.product.price * self.qauntity
    
    
    def __str__(self):
        return f"{self.qauntity} X {self.product.price} in ordered  {self.order.ordered_id}" 