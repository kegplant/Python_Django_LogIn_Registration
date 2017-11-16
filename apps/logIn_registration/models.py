from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from django.db import models
class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['name']='first name should not be empty!'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='invalid email!'
        return errors
    def logIn_validator(self,postData):
        errors={}
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='invalid email!'
        return errors

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255,default='')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    # books=models.ManyToManyField(Books,related_name='authors')
    # notes=models.TextField(default='')



