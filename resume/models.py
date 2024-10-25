from django.db import models

# Create your models here.
class Resume(models.Model): 
  short_desc = models.TextField('Short Description of Resume')
  
