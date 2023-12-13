from django.db import models

# Create your models here.
class UploadImage(models.Model):
		file = models.FileField(upload_to='account/images/')