from django.shortcuts import render
from rest_framework import generics #type: ignore
from books.models import Book
from .serializers import BookSerializer #type: ignore

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
