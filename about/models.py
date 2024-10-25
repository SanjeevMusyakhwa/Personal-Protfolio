from django.db import models

# Create your models here.
class About(models.Model):
  STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'InActive')
  ]
  heading = models.TextField(blank=False, null=False, verbose_name="About Heading")
  title = models.CharField(max_length=200, verbose_name="About Title")
  description = models.TextField(blank=False, null=False, verbose_name="About Description")
  image = models.ImageField("About Image", upload_to='about/', blank=False, null=False)
  dob = models.DateField(verbose_name='Date of Birth')
  website = models.URLField()
  phone_number = models.BigIntegerField(default=0)
  city = models.CharField("City", max_length=200)
  age = models.IntegerField("Age", default=0)
  degree = models.CharField("Degree", max_length=255)
  email = models.EmailField("Email Address")
  Freelance = models.CharField(
    "Freelancing",
    default='Active',
    choices=STATUS_CHOICES,
    max_length=20
  )

  def __str__(self, *args, **kwargs):
    return f"{self.id} {self.title}"
  
  def __unicode__(self,*args, **kwargs):
    return f"{self.id} {self.title}"
