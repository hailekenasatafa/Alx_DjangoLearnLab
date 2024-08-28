from django.shortcuts import render
from .forms import BookSearchForm
from .models import Book
from .forms import ExampleForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get('q')
        if query:
            books = books.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

def form_example_view(request):
    form = BookSearchForm(request.POST or None)
    if form.is_valid():
        # Handle form submission
        pass
    return render(request, 'bookshelf/form_example.html', {'form': form})

 
 


def example_form_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # Process the form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # You can add logic to save the data or send an email here
    return render(request, 'bookshelf/form_example.html', {'form': form})

