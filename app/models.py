from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        if len(post_data['title']) == 0:
            errors['title'] = "Title cannot be empty."
        if len(post_data['network']) == 0:
            errors['network'] = "Network cannot be empty."
        if len(post_data['release_date']) == 0:
            errors['release_date'] = "Release date cannot be empty."
        else:
            if datetime.today()<datetime.strptime(post_data['release_date'], '%Y/%M/%d'):
                errors['release_date']="No dates in the future"
        if len(post_data['description']) == 0:
                errors['description'] = "Description cannot be empty."
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
