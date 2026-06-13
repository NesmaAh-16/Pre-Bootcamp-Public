from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # 1. Required & Length Checks
        name = postData.get('name', '').strip()
        if len(name) < 6:
            errors["name"] = "name should be at least 6 characters."
        desc = postData.get('description', '').strip()
        print(f"this is a description {desc}")
        if len(desc) < 16:
            
            errors["description"] = "Description must be at least 16 characters if provided."
        return errors
class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # 1. Required & Length Checks
        content = postData.get('content', '').strip()
        if len(content) < 6:
            errors["content"] = "content should be at least 6 characters."
        return errors

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()