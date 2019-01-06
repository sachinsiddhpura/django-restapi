from rest_framework import serializers
from restapi.models.profile import Profile 
from restapi.models.education import Education 
from restapi.models.project import Project, ProjectItem

class EducationSe(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = [
				'institute',
				'description',
				'start_year',
				'still',
				'end_year',
			]

class ProjectSe(serializers.ModelSerializer):

	class Meta:
		model = Project
		fields =['title','url','description',]

class ProjectItemSe(serializers.ModelSerializer):

	class Meta:
		model = ProjectItem
		fields = [
				'project',
				'contribution',
				'start_year',
				'still',
				'end_year',
			]

class ProfileSe(serializers.ModelSerializer):

	educations = EducationSe(many=True)

	class Meta:
		model = Profile
		fields = [
				'first_name',
				'middle_name',
				'last_name',
				'DOB',
				'email',
				'gender',
				'phone_number',
				'city',
				'website',
				'address',
				'educations'
				
			]