from django.db import models
from django.contrib.auth.models import User

"""
class Image(models.Model):
    image = models.FileField()
"""

class Picture(models.Model):
    description = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return self.description
