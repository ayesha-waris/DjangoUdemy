from django.shortcuts import render
from .models import Book
# Create your models here.

def index(request):
  books = Book.objects.all()
  return render(request, 'book_store/index.html',{
    "books": books
  })