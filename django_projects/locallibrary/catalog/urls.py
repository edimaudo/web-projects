from django.urls import path
from . import views

urlpatterns = [
	#index page
	path('', views.index, name='index'),
	#list of all books
	path('books/', views.BookListView.as_view(), name='books'),
	#individual book
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	#list of all authors
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	#individual author
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
	path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

]