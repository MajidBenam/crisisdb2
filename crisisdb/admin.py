from django.contrib import admin

from .models import Polity, Agr_Prod_Pop, Country, Rulertransition, Section, Subsection, Agr_Productivity, Agr_Prod_Per_Pop, Citation, Reference, Majid

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Polity)
admin.site.register(Country)
admin.site.register(Agr_Prod_Pop)
admin.site.register(Agr_Productivity)
admin.site.register(Agr_Prod_Per_Pop)
admin.site.register(Citation)
admin.site.register(Reference)
admin.site.register(Rulertransition)
admin.site.register(Majid)
