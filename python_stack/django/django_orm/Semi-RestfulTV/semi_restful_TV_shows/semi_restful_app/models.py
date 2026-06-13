from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData, current_show_id=None):
        errors = {}
        
        # 1. Required & Length Checks
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters."
        
        # 2. Ninja Bonus: Description is optional, but if present must be 10+ chars
        desc = postData.get('description', '')
        if len(desc) > 0 and len(desc) < 10:
            errors["description"] = "Description must be at least 10 characters if provided."

        # 3. Ninja Bonus: Release Date must be in the past
        if not postData['release_date']:
            errors["release_date"] = "Release date is required."
        else:
            # Convert string from form into a date object to compare
            release_date = datetime.strptime(postData['release_date'], '%Y-%m-%d')
            if release_date > datetime.now():
                errors["release_date"] = "Release date must be in the past."

        # 4. Sensei Bonus: Title Uniqueness
        # Filter for shows with this title
        duplicate_list = self.filter(title=postData['title'])
        # If we are UPDATING, exclude the current show from the search
        if current_show_id:
            duplicate_list = duplicate_list.exclude(id=current_show_id)
        
        if duplicate_list.exists():
            errors["unique"] = "A TV show with this title already exists."

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() # Link the manager