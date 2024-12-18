from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import About
from Profile_app.models import Profile
from stats.models import Stats
from skill.models import *
from portfolio.models import *
from resume.models import *
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
  
  def get_skill_obj(self, *args, **kwargs):
    skill_obj = Skill.objects.first()
    if not skill_obj:
        return {'skill': None, 'skilldata': []}

    skills = {
        'skill': skill_obj,
        'skilldata': skill_obj.data.all()
    }
    return skills
  
  def get_resume_obj(self, *args, **kwargs):
    # Get sections
    education_section = ResumeSection.objects.filter(section_type="education").first()
    experience_section = ResumeSection.objects.filter(section_type="experience").first()

    # Populate entries by section type
    resumes = {
        'education_entries': education_section.entries.all() if education_section else [],
        'experience_entries': experience_section.entries.all() if experience_section else [],
    }
    return resumes

  
  def get_portfolio_obj(self,*args, **kwargs):
      portfolio_obj = Protfolio.objects.all()
      return portfolio_obj
  
  def get_context_data(self, **kwargs):
      context = super(Home, self).get_context_data(**kwargs)
      context["about_objs"] = self.get_about_obj()
      context["profile_objs"] = self.get_profile_obj()
      context["stat_objs"] = self.get_stat_obj()
      context['skills'] = self.get_skill_obj()
      context['resumes'] = self.get_resume_obj()
      context['portfolio_objs'] = self.get_portfolio_obj()
      return context
  
  
