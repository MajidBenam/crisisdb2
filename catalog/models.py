from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User

from django.urls import reverse

from datetime import date

import uuid

from django.utils import translation


class Genre(models.Model):
    """Model Representing a book Genre"""
    name = models.CharField(
        max_length=200, help_text='Enter a book Genre Please...')

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class ImportantPerson(models.Model):
    name = models.CharField(
        max_length=200, help_text='Enter a book Genre Please...')
    pic = models.ImageField(null=True, blank=True,)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Quote(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    owner = models.CharField(max_length=200,
                             help_text="Enter the person who said it.")
    description = models.TextField(null=True, blank=True)
    owner_real = models.ForeignKey(
        ImportantPerson, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        if self.description:
            return '{0}, {1}'.format(self.owner, self.description[:20])
        else:
            return self.owner


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Book(models.Model):
    """model representing a book"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description")
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)

    pic = models.ImageField(null=True, blank=True,)

    class Meta:
        ordering = ['title', 'author']

    def display_genre(self):
        """creates a string for the genre. This is required for a ManyToMany kind of link in Admin site"""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    # I think it is for Admin site as well.
    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance"""
        return reverse('book-detail', args=[str(self.id)])
        # the above aczually uses self.id to create a customized url

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    """Model representing an Author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pic = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class BookInstance(models.Model):
    """Model representing a specific copy of a book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique Id for this particular book")
    book = models.ForeignKey(
        'Book', on_delete=models.SET_NULL, null=True, related_name="bookinst")
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    page_numbers = models.IntegerField(null=True, blank=True)
    borrower = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    # Django automatically creates a method get_FOO_display() for every choices field "Foo" in a model, which can be used to get the current value of the field. (look at how thi is used in book_detail.html template)
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='d', help_text='Availablility')

    class Meta:
        ordering = ['due_back', ]
        permissions = (("can_mark_returned", "Set book as returned"),
                       ("can_renew", "Can Renew A Book"),)

    def __str__(self) -> str:
        """String for representing the Model Object"""
        return '{0} ({1})'.format(self.id, self.book.title)
