from django.shortcuts import render


from .models import Mineral
# Create your views here.

def index(request):
	return render(request, 'mineral_catalog_list.html')

#def mineral_catalog(request):
#	"""View function for home page of site."""
#	return render(request, 'mineral_catalog_list.html')


def mineral_catalog_list(request):
	m_list = Mineral.objects.all()
	context = {'mineral_list':m_list}
	return render(request, 'mineral_catalog_list.html',context)



