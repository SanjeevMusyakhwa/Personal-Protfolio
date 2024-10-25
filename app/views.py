from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import About
from Profile_app.models import Profile
from stats.models import Stats
# Create your views here.
class Home(TemplateView):
  template_name = 'index.html'
  

  def get_about_obj(self, *args, **kwargs):
     obj = About.objects.first()
     return obj
  
  def get_profile_obj(self,*args, **kwargs):
     profile_obj = Profile.objects.first()
     return profile_obj
  
  def get_stat_obj(self, *args, **kwargs):
     stat_obj = Stats.objects.first()
     return stat_obj

  def get_context_data(self, **kwargs):
      context = super(Home, self).get_context_data(**kwargs)
      context["about_objs"] = self.get_about_obj
      context["profile_objs"] = self.get_profile_obj
      context["stat_objs"] = self.get_stat_obj
      return context
  
  
