from django.db import models

# Create your models here.
class Stats(models.Model):
  description = models.TextField('Short Description', blank=True, null=True)
  clients_count = models.IntegerField("happy Clients", default=1)
  projects = models.IntegerField("Projects", default=1)
  hours_support = models.IntegerField('Hours of Support', default=1)
  awards = models.IntegerField('Awards', default=1)

  def __str__(self,*args, **kwargs):
    return f"{self.id} {self.clients_count}"

