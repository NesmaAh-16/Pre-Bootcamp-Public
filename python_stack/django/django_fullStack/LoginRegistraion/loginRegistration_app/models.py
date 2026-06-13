from django.db import models
import re
from datetime import datetime, date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # Name Validations
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name should be at least 2 characters and letters only."
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last name should be at least 2 characters and letters only."
        
        # Email Validations
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        elif User.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email is already in use."

        # Password Validations
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Passwords do not match."

        # Birthday & COPPA (13+ years old) Bonus
        if not postData['birthday']:
            errors['birthday'] = "Birthday is required."
        else:
            bday = datetime.strptime(postData['birthday'], '%Y-%m-%d').date()
            if bday >= date.today():
                errors['birthday'] = "Birthday must be in the past."
            else:
                age = (date.today() - bday).days // 365
                if age < 13:
                    errors['birthday'] = "You must be at least 13 years old to register."
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()