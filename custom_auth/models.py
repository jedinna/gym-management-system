from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.
class roll(models.Model):
    roll= models.CharField(max_length=80, primary_key=True)
    def __str__(self):
        return self.roll
class userManager(BaseUserManager):
    def create_user(self,email,first_name,last_name, password=None):
        if not email:
            raise ValueError('Users must have an email adress.')
        if not first_name or not last_name:
            raise ValueError('Users must have an FullName adress.')
        if not password:
            raise ValueError('Users must have an password adress.')
        user = self.model(
            email= self.normalize_email(email),
            first_name = first_name,
            last_name= last_name,
            
        )
        user.set_password(password)
        user.save(using= self.db)
        return user
    def create_superuser(self,email,first_name,last_name, password):
        user = self.create_user(
            email= self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin= True
        user.is_staff= True
        user.is_superuser= True
        user.save(using= self.db)
        return user

class users(AbstractBaseUser):

    first_name= models.CharField(max_length=50, null=False)

    last_name= models.CharField(max_length=50, null=False)
    user_name= models.CharField(max_length=50, null=False)
    email= models.EmailField(unique=True, max_length=254, primary_key=True)
    phone_no= models.CharField(max_length=50, null=False)
    roll= models.CharField(max_length=50, null=False)
    date_joined= models.DateTimeField(auto_now_add= True)
    last_login= models.DateTimeField(auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects= userManager()


    def __str__(self):
        return self.email
    def has_perm(self, perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    def has_change_permission(self,request, obj=None):
        return True
    def has_delete_permission(self,request, obj=None):
        return True
