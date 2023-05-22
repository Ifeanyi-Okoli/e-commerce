from django.db import models
from typing import Any, Dict, List, Union
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from core.models import Store
# from uuid import uuid4
# from core.account.models import Profile
# Create your models here.

class ProfileManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_seller(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        
        email = self.normalize_email(email)
        
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", False)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_seller", True)
        
                
        seller = self._create_user(email=email, **other_fields)
        store = Store(owner = seller, name=other_fields.name, tagline = other_fields.tagline)
        return seller, store


    def create_superuser(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        
        email = self.normalize_email(email)
        
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_seller", True)
        other_fields.setdefault("is_admin", True)
        user = self.create_user(email=email, username=username, password=password, **other_fields)
        
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")
        # return self._create_user(email, username, password, **other_fields)
        return user


class Profile(AbstractUser):
    # id=models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name", "username", "password")
    
    objects = ProfileManager()
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True