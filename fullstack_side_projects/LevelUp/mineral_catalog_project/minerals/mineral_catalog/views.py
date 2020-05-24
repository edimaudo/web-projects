from django.shortcuts import render


from mineral_catalog.models import Mineral
# Create your views here.
def index(request):
	"""View function for home page of site."""
	return render(request, 'index.html')
