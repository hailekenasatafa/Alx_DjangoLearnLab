from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from .forms import BookSearchForm

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' 


def form_example_view(request):
    form = BookSearchForm(request.POST or None)
    if form.is_valid():
        # Handle the form submission (e.g., process data, save to database)
        pass
    return render(request, 'bookshelf/form_example.html', {'form': form})
