from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Images_info(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=200)
    image_pub_date = models.DateTimeField('date published')
    image_data = models.ImageField(blank=True, upload_to="images", null=True)

    def __str__(self):
        return self.image_title