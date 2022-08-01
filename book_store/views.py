from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min
# Create your models here.


def index(request):
    books = Book.objects.all().order_by("title")
    count = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, 'book_store/index.html', {
        "books": books,
        "total_books": count,
        "avg_rating": avg_rating,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #   raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_store/book_detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating
    })
