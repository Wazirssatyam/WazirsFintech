from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email,username ,mobile_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not mobile_number:
            raise ValueError('Users must have a mobile_number')    

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            mobile_number=mobile_number,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,mobile_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,username=username,mobile_number=mobile_number
           
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    
    otp = models.IntegerField(null=True, blank=True) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','mobile_number']

    objects = MyAccountManager()

# Create your models here.
class slider(models.Model):
    caption=models.CharField(max_length=150,null=True)
    image_text=models.TextField()
    image=models.ImageField(upload_to="media/")
    def __str__(self) :
        return self.caption
class team(models.Model):
    name=models.CharField(max_length=150,null=True)
    designation=models.CharField(max_length=150,null=True)
    brief=models.TextField()
    twitter=models.CharField(max_length=150,null=True)
    facebook=models.CharField(max_length=150,null=True)
    instagram=models.CharField(max_length=150,null=True)
    linkedn=models.CharField(max_length=150,null=True)
    image=models.ImageField(upload_to="media/")