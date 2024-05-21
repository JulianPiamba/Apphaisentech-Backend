from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    user = models.AutoField(primary_key=True)
    usr_name = models.CharField(max_length=200)
    usr_last_name = models.CharField(max_length=200)
    usr_gener = models.CharField(max_length=50)
    usr_email = models.EmailField(max_length=150)
    usr_password = models.CharField(max_length=50)
    usr_address = models.CharField(max_length=200)
    usr_phone = models.CharField(max_length=200)
    usr_last_access = models.DateTimeField(auto_now=True)
    
class Role (models.Model):
    rol_name = models.CharField(max_length=100)
    rol_description = models.TextField(max_length=100)
    def __str__(self):
        return self.rol_name
    
class Product(models.Model):
    product = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=200)
    pro_price = models.CharField(max_length=200)
    pro_description = models.TextField(max_length=100)
    pro_review = models.IntegerField()
    pro_stock = models.PositiveIntegerField()
    pro_image = models.CharField(max_length=100)
    pro_category = models.CharField(max_length=200)
    
    
    
class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    sale_total_amount = models.DecimalField(max_digits=10, decimal_places= 2)
    sale_date = models.DateTimeField(auto_now_add=True)
    

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete = models.CASCADE)
    product = models.ForeignKey(Product,  on_delete = models.CASCADE)
    sale_quantity = models.PositiveBigIntegerField() #Cantidad de productos Vendidos
    sale_price = models.DecimalField(max_digits=10, decimal_places=2) #Precio de cada producto Vendido
    
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    rw_rating = models.PositiveBigIntegerField()
    rw_comment = models.TextField(max_length=200)
    rw_date = models.DateTimeField(auto_now_add=True)
    
class PaymentMethod(models.Model):
    pym_method = models.CharField(max_length=100)
    pym_icon = models.ImageField
    
    def __str__(self):
        return self.pym_method
    
class PaymentHistory(models.Model):
    pyh_amount = models.DecimalField(max_digits=10,decimal_places=2)
    pym_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pym_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    
class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_products = models.ManyToManyField(Product, through='ShoppingCartItem')
    
class ShoppingCartItem(models.Model):
    ShoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)     
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoI_quantity = models.PositiveBigIntegerField()
    
    
    