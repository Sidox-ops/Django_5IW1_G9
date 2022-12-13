from django.urls import path

from .views import books

urlpatterns = [
    path('books/', books.book_list, name='book_list'),
    path('books/view/<int:pk>', books.book_view, name='book_view'),
    path('books/new', books.book_create, name='book_new'),
    path('books/view/<int:pk>', books.book_view, name='book_view'),
    path('books/edit/<int:pk>', books.book_update, name='book_edit'),
    path('books/delete/<int:pk>', books.book_delete, name='book_delete'),
]