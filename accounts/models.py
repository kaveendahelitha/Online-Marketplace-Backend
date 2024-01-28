from django.db import models

#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#
#class UserAccountManager(BaseUserManager):
#      # creating normal user
#    def create_user(self, email, name, password=None,**extra_fields):
#        if not email:
#            raise ValueError('User must have an email address')
#
#        email = self.normalize_email(email)
#        user = self.model(email=email, **extra_fields)
#
#       #hash password
#        user.set_password(password)  
#
#        user.save()
#        return user
#    def create_superuser(self, email, name, password):
#       
#        user = self.create_user(email,
#            password=password,
#            name=name
#        )
#        user.is_admin = True
#        user.save()
#        return user
#    
#      
#class UserAccount(AbstractBaseUser, PermissionsMixin):
#    email = models.EmailField(max_length=255, unique=True)
#    first_name = models.CharField(max_length=30, default='') 
#    last_name = models.CharField(max_length=30, default='')
#    is_active = models.BooleanField(default=True)
#    is_staff = models.BooleanField(default=False)
#
#    objects = UserAccountManager()
#
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['first_name', 'last_name']
#
#    def get_full_name(self):
#        return self.name
#
#    def get_short_name(self):
#        return self.name
#
#    def __str__(self):
#        return self.email
#