from platform import mac_ver
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class CandidateInfo(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    phoneNo = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=20)


    class Meta:
        db_table = 'CandidateInfo'

class CompanyInfo(models.Model):
    companyName = models.CharField(max_length=20)
    companyOwnerName = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    companyLogo = models.ImageField(upload_to='img')
    class Meta:
        db_table = 'ComapnyInfo'
        
class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'AboutUs'



class Employee(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(unique=True,null=True,blank=False)
    password = models.CharField(max_length=15)
    mobileNo = models.CharField(max_length=10)
    AadharNo = models.CharField(max_length=16)

    class Meta:
        db_table = "EmployeeInfo"
    
