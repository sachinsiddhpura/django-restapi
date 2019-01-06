from django.db import models 
from .profile import Profile
from django.utils.translation import ugettext_lazy as _
from restapi import data

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=_("title"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))
    url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))

    class Meta:
        app_label = 'restapi'

    def __str__(self):
        return self.title


class ProjectItem(models.Model):
    persondata = models.ForeignKey(Profile, related_name='projectitems',on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='items',on_delete=models.CASCADE)
    contribution = models.TextField(max_length=3000, blank=True, verbose_name=_("contribution"))

    start_year = models.IntegerField(choices=data.YEARS, default=data.current_year, verbose_name=_("start year"))
    start_month = models.IntegerField(choices=data.MONTHS, default=data.current_month, verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still contributor"))
    end_year = models.IntegerField(choices=data.YEARS, null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(choices=data.MONTHS, null=True, blank=True, verbose_name=_("end month"))

    weight = models.IntegerField(choices=data.WEIGHTS, default=1, verbose_name=_("weight"))

    class Meta:
        app_label = 'restapi'
        unique_together = ('persondata', 'project')

    def __str__(self):
        return self.project.title
