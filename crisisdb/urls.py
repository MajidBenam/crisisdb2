from django.urls import path
from .models import Agr_Prod_Pop, Polity, Rulertransition
from django.views.generic.list import ListView

from . import views
from.views import PolityAutocomplete, CitationAutocomplete

urlpatterns = [
    path('', views.crisisdbindex, name='crisisdb-index'),
    # path('vars/', views.crisisdbvars, name='crisisdb-vars'),
    path('vars/', views.CrisisDBVarsView.as_view(), name='crisisdb-vars'),
    path('ajax/load-subsections/', views.load_subsections,
         name='ajax_load_subsections'),

]
# get_context_data: {"agr_list": Agr_Prod_Pop.objects.all(),
# "rul_list": Rulertransition.objects.all(),
# and so on for all the desired models...
#  }
urlpatterns += [
    path('Agr_Prod_Pops/', views.Agr_Prod_PopListView.as_view(), name='Agr_Prod_Pops'),
    path('Agr_Prod_Pop/<int:pk>', views.Agr_Prod_PopDetailView.as_view(),
         name='Agr_Prod_Pop-detail'),
    path('Agr_Prod_Pop/create/', views.Agr_Prod_PopCreate.as_view(),
         name="Agr_Prod_Pop-create"),
    path('Agr_Prod_Pop/<int:pk>/update/',
         views.Agr_Prod_PopUpdate.as_view(), name="Agr_Prod_Pop-update"),
    path('Agr_Prod_Pop/<int:pk>/delete/',
         views.Agr_Prod_PopDelete.as_view(), name="Agr_Prod_Pop-delete"),
    # Download
    path('agrprodpopdownload/', views.agr_prod_pop_download,
         name="agr_prod_pop-download"),

]

urlpatterns += [
    path('variable_<str:mymodel>', views.mytest,
         name='mytest'),
]

urlpatterns += [
    path('rulertransitions/', views.RulertransitionListView.as_view(),
         name='rulertransitions'),
    path('rulertransition/<int:pk>', views.RulertransitionDetailView.as_view(),
         name='rulertransition-detail'),
    path('rulertransition/create/', views.RulertransitionCreate.as_view(),
         name="rulertransition-create"),
    path('rulertransition/<int:pk>/update/',
         views.RulertransitionUpdate.as_view(), name="rulertransition-update"),
    path('rulertransition/<int:pk>/delete/',
         views.RulertransitionDelete.as_view(), name="rulertransition-delete"),
]


urlpatterns += [
    path(
        'polity-autocomplete/',
        PolityAutocomplete.as_view(),
        name='polity-autocomplete',
    ),
    path(
        'citation-autocomplete/',
        CitationAutocomplete.as_view(),
        name='citation-autocomplete',
    ),
]
