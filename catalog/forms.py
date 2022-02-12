import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from catalog.models import BookInstance, Book, Author

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date (default 3 weeks)')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid Date - renewal more than 4 weeks ahead'))

        return data


class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {
            'due_back': _('New Renewal Date')
        }
        help_texts = {
            'due_back': _('enter a new date please')
        }


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['isbn'].help_text = None
        self.fields['genre'].help_text = None
        self.fields['summary'].help_text = None
        self.fields['genre'].label = "Genre (Hold CTRL to select multiple)"
        self.fields['pic'].label = 'Please choose a picture:'

    class Meta:
        model = Book
        fields = ('title', 'author',
                  'isbn', 'genre', 'language', 'pic', 'summary', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control  mb-3', 'placeholder': 'Enter Book Name'}),
            'author': forms.Select(attrs={'class': 'form-control  mb-3', }),
            'summary': forms.Textarea(attrs={'class': 'form-control  mb-3', 'placeholder': 'Enter a summary'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control  mb-3', 'placeholder': '12345678912fe'}),
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'mb-2', }),
            'language': forms.RadioSelect(attrs={'class': 'mb-2', }),
            'pic': forms.FileInput(attrs={'class': 'form-control  mb-3', }),
        }
