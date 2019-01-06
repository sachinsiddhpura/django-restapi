from rest_framework import generics
from .serializer import ProfileSe
from rest_framework.filters import SearchFilter
from restapi.models.profile import Profile 

class Restapi(generics.ListAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSe

	backend_filter = [SearchFilter]
	search_field = 'first_name'
