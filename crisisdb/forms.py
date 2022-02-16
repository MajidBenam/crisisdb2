import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea
from crisisdb.models import Agr_Prod_Pop, Citation, Rulertransition
#from crispy_forms.helper import FormHelper

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

#from django_select2 import forms as s2forms


# class CitationsWidget(s2forms.ModelSelect2MultipleWidget):
#     search_fields = [
#         "Citation.ref__icontains",
#     ]
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class RulertransitionForm(forms.ModelForm):
    class Meta:
        model = Rulertransition
        fields = ('polity', 'predecessor', 'successor', 'start_reign_predecessor',
                  'end_reign_transition', 'reign_number_predecessor', 'contested',
                  'overturn', 'assassination_predecessor', 'intra_elite', 'military_revolt',
                  'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', 'conflict_name', 'transition_label', 'description', 'finalized', 'citations', 'name')

        # make sure the id that is selected here for name and section matches reality ALL the TIME
        widgets = {
            'conflict_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
            'transition_label': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
            'polity': forms.Select(attrs={'class': 'form-control  mb-3', }),
            'predecessor': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
            'successor': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
            'start_reign_predecessor': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
            'end_reign_transition': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),


            'reign_number_predecessor': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),

            'contested': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'overturn': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'assassination_predecessor': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'intra_elite': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'military_revolt': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'popular_uprising': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'separatist_rebellion': forms.Select(attrs={'class': 'form-control  mb-3', }),

            'external_invasion': forms.Select(attrs={'class': 'form-control  mb-3', }),
            'external_interference': forms.Select(attrs={'class': 'form-control  mb-3', }),


            'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px'}),
            'citations': forms.SelectMultiple(attrs={'class': 'form-control  mb-3',  'style': 'height: 140px'}),
            'finalized': forms.CheckboxInput(attrs={'class': ' mb-3', 'checked': True, }),
            # 'citation_2': forms.Select(attrs={'class': 'form-control  mb-3', }),
        }


class Agr_Prod_PopForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Agr_Prod_PopForm, self).__init__(*args, **kwargs)
        # maybe we can use similar technique as below to feed the form with more data here
        # in the form of a dictionary and then iterate in the template
        self.full_name = 'Agricultural_production_and_population'
    # to read the above in template (very easy)
    # {% for key, value in form.mydic.items %}
    #   <h4>{{ key }}: {{ value }}</h4>
    # {% endfor %}

    # mycitations = forms.ModelMultipleChoiceField(
    #     # widget=Select2MultipleWidget,
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Citation.objects.all(),
    #     #empty_label="Choose a citation",
    # )
    # allcitations = forms.ModelChoiceField(
    #     # widget=Select2MultipleWidget,
    #     widget=forms.Select,
    #     queryset=Citation.objects.all(),
    #     #empty_label="Choose a citation",
    # )

    # xyz = forms.ModelMultipleChoiceField(
    #     queryset=Citation.objects.all(), widget=forms.SelectMultiple)

    # mycitations2 = forms.ModelMultipleChoiceField(label=_('Citations'), queryset=Citation.objects.all(
    # ), required=False, widget=FilteredSelectMultiple(_('citations'), True))

    class Meta:
        model = Agr_Prod_Pop
        fields = ('polity', 'section', 'subsection',
                  'year_from', 'year_to', 'total_population', 'arable_land_per_capita', 'description', 'tag', 'finalized', 'citations')
        labels = {
            'year_from': 'Start Year',
            'year_to': 'End Year',
            'tag': 'Certainty',
            'citations': 'Add one or more Citations',
            'finalized': 'This piece of data is verified.',
            'arable_land_per_capita': 'Arable Land (per capita)',
            'total_population': 'Total Population',
        }

        # make sure the id that is selected here for subsection and section matches reality ALL the TIME
        widgets = {
            'polity': forms.Select(attrs={'class': 'form-control  mb-3', }),
            'section': forms.Select(attrs={'class': 'form-control  mb-3', 'readonly': True, 'selected': True, }),
            'subsection': forms.Select(attrs={'class': 'form-control  mb-3', 'readonly': True, 'selected': True, }),
            'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
            'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
            'total_population': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
            'arable_land_per_capita': forms.NumberInput(attrs={'step': 0.01}),
            'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px'}),
            'citations': forms.SelectMultiple(attrs={'class': 'form-control  mb-3',  'style': 'height: 140px'}),
            'tag': forms.RadioSelect(attrs={'class': 'form-control  mb-3', }),
            'finalized': forms.CheckboxInput(attrs={'class': ' mb-3', 'checked': True, }),
            # 'citation_2': forms.Select(attrs={'class': 'form-control  mb-3', }),
        }

        initial = {
            'section': 1,
            'subsection': 1,
        }
        # helper = FormHelper()
        # helper.form_method = 'POST'
        # helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))
