from django.db import models

# ResumeSection model
class ResumeSection(models.Model):
    SECTION_CHOICES = [
        ('education', 'Education'),
        ('experience', 'Professional Experience'),
        
        # Add more sections as needed
    ]

    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES, unique=True)

    def __str__(self):
        return self.section_type.capitalize()

# ResumeEntry model
class ResumeEntry(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField('Position or Degree Title', max_length=200)
    institution_name = models.CharField('Institution or Company', max_length=200)
    start_date = models.DateField('Start Date', blank=False, null=False)
    end_date = models.DateField('End Date', blank=True, null=True)
    location = models.CharField('Location', max_length=200)
    description = models.TextField('Description', blank=True)

    def __str__(self):
        return f"{self.title} at {self.institution_name}"
