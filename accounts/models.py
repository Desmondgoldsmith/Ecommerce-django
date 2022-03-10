from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class accounts(AbstractBaseUser):
    firstName = models.charField(max_length=40)
    lastname = models.charField(max_length=70)
    username = models.charField(max_length=70, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    phoneNumber = models.charField(max_length=20)
    datejoined = models.DateTimeField(auto_now_add=True)
    lastlogin = models.DateTimeField(auto_now_add=True)
    isAdmin = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isStaff = models.BooleanField(default=False)
    isSuperUser = models.BooleanField(default=False)
# loginin with your email
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['userName','firstName','lastName']


    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.isAdmin
    
    def has_module_perm(self,add_label):
        return True
    
