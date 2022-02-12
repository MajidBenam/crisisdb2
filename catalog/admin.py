from django.contrib import admin

from .models import Author, BookInstance, Genre, Book, BookInstance, Language, Quote, ImportantPerson

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Quote)
admin.site.register(ImportantPerson)

admin.site.register(Language)


class BookStatusFilter(admin.SimpleListFilter):
    title = "Book Status"
    parameter_name = "bookinst"

    def lookups(self, request, model_admin):
        return [
            ("Good_to_Go", "I am Good to go"),
            ("Bad_to_Go", "Naaah"),
        ]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value() == "Good_to_Go":
            return queryset.distinct().filter(status__in=['a', 'd'])
        if self.value() == "Bad_to_Go":
            return queryset.distinct().filter(status__in=['o', 'r'])


class PageNumbersFilter(admin.SimpleListFilter):
    title = "Page Number Status"
    parameter_name = "pagenum"

    def lookups(self, request, model_admin):
        return [
            ("Good_to_Go", "> 50 and < 100"),
            ("Bad_to_Go", "< 50"),
        ]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value() == "Good_to_Go":
            return queryset.distinct().filter(page_numbers__gte=50).filter(page_numbers__lte=100)
        if self.value() == "Bad_to_Go":
            return queryset.distinct().filter(page_numbers__lt=50)


class BooksInline(admin.TabularInline):
    """Defines format of Inline book insertion (used in the inlines of AuthorAdmin)"""
    model = Book
    exclude = ['summary', ]
    extra = 0


class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in the inlines of BookAdmin)"""
    model = BookInstance
    exclude = ['id', ]
    readonly_fields = ['imprint', 'borrower', ]
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administation object for Author models.
     - Fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - inline addition of books in author view (inlines) 
     """
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', 'pic',
              ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'display_genre')
    #fields = ['title', 'author', 'pic', ]
    #inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration Object for BookInstance models
      - fields to be displayed in list view (list_display)
      - filters that will be displayed in sidebar (list_filter)
      - grouping of fields into sections (fieldsets)
      """
    list_display = ('book', 'status', 'borrower', 'due_back', 'page_numbers')
    list_filter = (BookStatusFilter, PageNumbersFilter)

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'page_numbers')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
    )
