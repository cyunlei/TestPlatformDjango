from django.urls import path
from . import views

urlpatterns = {
    path("", view=views.home, name='home'),
    path("api/books/", view=views.books, name='book_list'),
}

