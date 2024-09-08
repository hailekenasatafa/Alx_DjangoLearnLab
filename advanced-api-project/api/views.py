from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView to retrieve all books and CreateView to add a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Customize behavior if needed (e.g., overriding perform_create)
    def perform_create(self, serializer):
        # Custom logic during book creation (if needed)
        serializer.save()

# DetailView to retrieve, update, or delete a book by ID
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Custom logic during update (e.g., updating timestamp)
        serializer.save()

    def perform_destroy(self, instance):
        # Custom logic during deletion (if needed)
        instance.delete()
