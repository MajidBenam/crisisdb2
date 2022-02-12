from django.urls import path

from . import views

urlpatterns = [
    path('', views.crisisdbindex, name='crisisdb-index'),
    path('vars/', views.crisisdbvars, name='crisisdb-vars'),
]

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
