from django.urls import path

from .views import books, authors, collections, genres, editors,libraries

urlpatterns = [
    path('books/', books.book_list, name='book_list'),
    path('books/view/<int:pk>', books.book_view, name='book_view'),
    path('books/new', books.book_create, name='book_new'),
    path('books/view/<int:pk>', books.book_view, name='book_view'),
    path('books/edit/<int:pk>', books.book_update, name='book_edit'),
    path('books/delete/<int:pk>', books.book_delete, name='book_delete'),

    path('collections/', collections.collection_list, name='collection_list'),
    path('collections/view/<int:pk>', collections.collection_view, name='collection_view'),
    path('collections/new', collections.collection_create, name='collection_new'),
    path('collections/view/<int:pk>', collections.collection_view, name='collection_view'),
    path('collections/edit/<int:pk>', collections.collection_update, name='collection_edit'),
    path('collections/delete/<int:pk>', collections.collection_delete, name='collection_delete'),

    path('authors/', authors.author_list, name='author_list'),
    path('authors/view/<int:pk>', authors.author_view, name='author_view'),
    path('authors/new', authors.author_create, name='author_new'),
    path('authors/view/<int:pk>', authors.author_view, name='author_view'),
    path('authors/edit/<int:pk>', authors.author_update, name='author_edit'),
    path('authors/delete/<int:pk>', authors.author_delete, name='author_delete'),

    path('genres/', genres.genre_list, name='genre_list'),
    path('genres/view/<int:pk>', genres.genre_view, name='genre_view'),
    path('genres/new', genres.genre_create, name='genre_new'),
    path('genres/view/<int:pk>', genres.genre_view, name='genre_view'),
    path('genres/edit/<int:pk>', genres.genre_update, name='genre_edit'),
    path('genres/delete/<int:pk>', genres.genre_delete, name='genre_delete'),

    path('editors/', editors.editor_list, name='editor_list'),
    path('editors/view/<int:pk>', editors.editor_view, name='editor_view'),
    path('editors/new', editors.editor_create, name='editor_new'),
    path('editors/view/<int:pk>', editors.editor_view, name='editor_view'),
    path('editors/edit/<int:pk>', editors.editor_update, name='editor_edit'),
    path('editors/delete/<int:pk>', editors.editor_delete, name='editor_delete'),

    path('libraries/', libraries.library_list, name='library_list'),
    path('libraries/view/<int:pk>', libraries.library_view, name='library_view'),
    path('libraries/new', libraries.library_create, name='library_new'),
    path('libraries/view/<int:pk>', libraries.library_view, name='library_view'),
    path('libraries/edit/<int:pk>', libraries.library_update, name='library_edit'),
    path('libraries/delete/<int:pk>', libraries.library_delete, name='library_delete'),
    

    
]