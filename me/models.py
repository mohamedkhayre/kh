from django.db import models
from django.contrib.auth.models import User, auth
#from django.contrib.auth.models import AbstractUser


# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='images/imagess/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Blogg(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	usernam=models.CharField(max_length=100)
	#emaill=models.CharField(max_length=100)
	passwor=models.CharField(max_length=100)
	is_active = models.BooleanField( default=True)

	def __str__(self):
		return self.usernam +' | '+ self.passwor
	objects= models.Manager()
	
class billmount(models.Model):
	daySpent=models.IntegerField(max_length=100,blank=False)
	roomCharge=models.IntegerField(max_length=100)
	cost=models.IntegerField(max_length=100)
	bFee=models.IntegerField(max_length=100)
	otherCharge=models.IntegerField(max_length=100)
	total=models.IntegerField(max_length=100)
    #empAuth_objects=models.Manager()
	
class exceldata(models.Model):
	idd=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	