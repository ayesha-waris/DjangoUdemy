from django.contrib import admin

from .models import Address, Author, Book, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "author")}
    list_filter = ("author", "rating")
    list_display = ("author", "title")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city")


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name","code")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country,CountryAdmin)
