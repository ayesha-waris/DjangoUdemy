from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title","author")}
  list_filter = ("author", "rating")
  list_display = ("author","title")

admin.site.register(Book, BookAdmin)

