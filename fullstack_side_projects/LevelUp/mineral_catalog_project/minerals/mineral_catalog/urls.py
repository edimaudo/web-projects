from django.urls import path
from . import views

urlpatterns = [
    path('', views.mineral_catalog_list, name='index'),
    path('mineral_catalog/',views.mineral_catalog_list,name='mineral_catalog'),

]