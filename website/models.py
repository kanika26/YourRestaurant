from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


# Create your models here.
class dish(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    img1 = models.ImageField(upload_to='media')
    img2 = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Pcategory=models.CharField(max_length=300)
    Scategory= models.CharField(max_length=300)
    available = models.CharField(max_length=200)
    value_for_two = models.IntegerField()


    class Meta:
        db_table = 'data'



    def __str__(self):
        return str(self.title)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)


    def __str__(self):
        return self.username

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    img1 = models.ImageField(upload_to='media')
    img2 = models.ImageField(upload_to='media')
    price = models.CharField(max_length=300)
    Pcategory = models.CharField(max_length=300)
    Scategory = models.CharField(max_length=300)
    available = models.CharField(max_length=200)
    quantity = models.IntegerField()
    userid = models.CharField(max_length=300)

    class Meta:
        db_table = "CartTable"



class CartObject(models.Model):
    cartid=models.AutoField(primary_key=True)
    producttitle=models.CharField(max_length=4500)
    productid = models.CharField(max_length=45)
    price = models.CharField(max_length=200)
    quantity=models.IntegerField()
    userid = models.CharField(max_length=100)


    class Meta:
        db_table="cartObject"



class onlineorderform(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=8)
    state = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        db_table = "orderform"

    def __str__(self):
        return self.name



