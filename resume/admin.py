from django.contrib import admin
from resume.models import *
# Register your models here.
class ResumeDataTabularInline(admin.TabularInline):
  model = ResumeEntry

class ResumeModelAdmin(admin.ModelAdmin):
  inlines = [ResumeDataTabularInline]

  class Meta:
    model = ResumeSection

admin.site.register(ResumeSection, ResumeModelAdmin)