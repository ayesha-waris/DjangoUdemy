from django.contrib import admin

from .models import Author, Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title","author")}
  list_filter = ("author", "rating")
  list_display = ("author","title")

class AuthorAdmin(admin.ModelAdmin):
  list_display = ("first_name","last_name")

admin.site.register(Book, BookAdmin)
admin.site.register(Author,AuthorAdmin)

