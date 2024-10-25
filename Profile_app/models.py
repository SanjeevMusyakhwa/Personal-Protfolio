from django.db import models

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=255, verbose_name='Full Name')
  typed = models.CharField('typed', max_length=255,help_text="Type Like This -> Designer, Developer, Freelancer, Photographer")
  facebook = models.URLField("Facebook")
  twitter = models.URLField("Twitter")
  linkedIn = models.URLField("LinkedIn")
  github = models.URLField("Github")
  instagram = models.URLField("Instagram")
  image = models.ImageField('About Profile', upload_to='profile/', blank=False, null=False)

  def __str__(self,*args, **kwargs):
    return f"{self.id} {self.name}"
