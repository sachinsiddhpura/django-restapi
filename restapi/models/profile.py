from django.db import models
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
	('M','Male'),
	('F','Female'),
	('O','Other'),
	)

class Profile(models.Model):
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    DOB = models.DateTimeField()
    profile_pic  = models.ImageField(upload_to='profile_pic')
    about = models.TextField()

    email = models.EmailField(max_length=100, unique=True, verbose_name=_("Email"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_("Gender"))
    phone_number = models.CharField(max_length=10, unique=True, verbose_name=_("Phone number"))
    website = models.URLField(max_length=50, blank=True, null=True, verbose_name=_("Website"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    country = models.CharField(max_length=50, verbose_name=_("Country"))
    state = models.CharField(max_length=50, verbose_name=_("State"))
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Address"))

    class Meta:
    	app_label = 'restapi'
    	verbose_name = _('Personal Data')

    def __str__(self):
    	return '{0} {1} - {2}'.format(self.first_name,self.last_name,self.title)