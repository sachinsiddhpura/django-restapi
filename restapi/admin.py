from django.contrib import admin

# Register your models here.
from restapi.models.profile import Profile
from restapi.models.education import Education 
from restapi.models.project import Project,ProjectItem

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(ProjectItem)