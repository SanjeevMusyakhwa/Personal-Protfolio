from django.db import models

# Create your models here.
class Protfolio(models.Model):
  short_description = models.TextField('Short Description')
  title = models.CharField(max_length=20)
  image = models.ImageField('Protfolio Image', upload_to='protfolio/')
  link = models.URLField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self,*args, **kwargs):
    return f"{self.id} {self.title}"