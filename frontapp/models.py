from django.db import models

# Create your models here.
class RegisterDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.IntegerField(null=True,blank=True)
    ConfirmPassword=models.IntegerField(null=True,blank=True)

class BookingDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Date=models.CharField(max_length=100,null=True,blank=True)
    Destination=models.CharField(max_length=100,null=True,blank=True)
    Person=models.CharField(max_length=100,null=True,blank=True)
    Kids=models.CharField(max_length=100,null=True,blank=True)

class ContactDB(models.Model):
    Name=models.CharField(max_length=100, null=True, blank=True)
    Email=models.CharField(max_length=100, null=True, blank=True)
    Subject=models.CharField(max_length=100, null=True, blank=True)
    Message=models.CharField(max_length=100, null=True, blank=True)



class SearchDB(models.Model):
    Thailand=models.CharField(max_length=100,null=True,blank=True)
    California=models.CharField(max_length=100,null=True,blank=True)
    Japan=models.CharField(max_length=100,null=True,blank=True)
    Turkey=models.CharField(max_length=100,null=True,blank=True)
    Venice=models.CharField(max_length=100,null=True,blank=True)
    Chinna=models.CharField(max_length=100,null=True,blank=True)
    Singapor=models.CharField(max_length=100,null=True,blank=True)










