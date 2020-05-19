from django.urls import path
from . import views

urlpatterns = [
	#index page
	path('', views.index, name='index'),
	#list of all books
	path('books/', views.BookListView.as_view(), name='books'),
	#individual book
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]