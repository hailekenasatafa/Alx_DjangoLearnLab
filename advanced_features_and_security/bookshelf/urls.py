from django.urls import path
from .views import search_books, form_example_view
from .views import example_form_view

urlpatterns = [
    path('search-books/', search_books, name='search_books'),
    path('form-example/', form_example_view, name='form_example'),
    path('example-form/', example_form_view, name='example_form'),
]

 

 