from django.urls import path
from . import views

urlpatterns = [
    path('', views.mineral_catalog, name='index'),
    path('mineral_catalog',views.mineral_catalog,name='mineral_catalog'),

]