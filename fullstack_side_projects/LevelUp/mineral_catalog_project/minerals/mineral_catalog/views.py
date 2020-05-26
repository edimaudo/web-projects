from django.shortcuts import render


from .models import Mineral
# Create your views here.

def index(request):
	return render(request, 'mineral_catalog_list.html')

def mineral_catalog(request):
	"""View function for home page of site."""
	return render(request, 'mineral_catalog_list.html')


class MineralListView(generic.ListView):
    model = Mineral
    context_object_name = 'my_mineral_list'   # your own name for the list as a template variable
    queryset = Mineral.objects.all() # Get 5 books containing the title war
    template_name = 'mineral_catalog_list.html'  # Specify your own template name/location



