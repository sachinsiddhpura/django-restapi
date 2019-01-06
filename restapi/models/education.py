
from django.db import models 
from .profile import Profile
from django.utils.translation import ugettext_lazy as _
from restapi import data

class Education(models.Model):
    personaldata = models.ForeignKey(Profile,on_delete=models.CASCADE)
    institute = models.CharField(max_length=120)
    description = models.TextField()

    start_year = models.IntegerField(choices=data.YEARS, default=data.current_year, verbose_name=_("Start year"))
    start_month = models.IntegerField(choices=data.MONTHS, default=data.current_month, verbose_name=_("Start month"))
    still = models.BooleanField(default=True, verbose_name=_("Currently studying"))
    end_year = models.IntegerField(choices=data.YEARS, null=True, blank=True, verbose_name=_("End year"))
    end_month = models.IntegerField(choices=data.MONTHS, null=True, blank=True, verbose_name=_("End month"))

    class Meta:
    	app_label = 'restapi'
    	ordering = ('-start_year',)

    def __str__(self):
    	return self.institute