from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search Books')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
