from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView


from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, response
from .models import Rulertransition, Agr_Prod_Pop, Citation, Reference, Agr_Productivity, Agr_Prod_Per_Pop, Polity, Section, Subsection

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from django.core.paginator import Paginator

from crisisdb.forms import Agr_Prod_PopForm, RulertransitionForm
from django.http import HttpResponse


crisisdb_vars_list = [Rulertransition, Agr_Prod_Pop]


def crisisdbindex(request):
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",

    }
    return render(request, 'crisisdb-index.html', context=context)


all_models_dict = {

}


def crisisdbvars(request):
    context = all_models_dict
    # {
    #     'list_of_vars': {
    #         'Agr_Prod_Pod': [Agr_Prod_Pop.objects.count(), "tractor", "{% url 'crisisdb-index' %}"],
    #         'RulerTransutions': [Rulertransition.objects.count(), "exchange-alt", "{% url 'crisisdb-index' %}"],
    #         'Polity': [Polity.objects.count(), "flag", "{% url 'crisisdb-index' %}"],
    #         'Citation': [Citation.objects.count(), "quote-left", "{% url 'crisisdb-index' %}"],
    #         'Reference': [Reference.objects.count(), "book", "{% url 'crisisdb-index' %}"],
    #         'Agr_Productivity':  [Agr_Productivity.objects.count(), "seedling", "{% url 'crisisdb-index' %}"],
    #         'Agr_Prod_Per_Pop': [Agr_Prod_Per_Pop.objects.count(), "leaf", "{% url 'crisisdb-index' %}"],
    #         'Section': [Section.objects.count(), "list", "{% url 'crisisdb-index' %}"],
    #         'Subsection': [Subsection.objects.count(), "clipboard-list", "{% url 'crisisdb-index' %}"],
    #         # 'Users': User.objects.count(),
    #     }
    # }
    return render(request, 'crisisdb_vars.html', context)


def mytest(request, mymodel, realmodel):
    data = realmodel.objects.all()
    context = {
        'greet': data,
    }
    return render(request, 'crisisdb/test_template.html', context=context)


############# Rulertransition ########################

class RulertransitionListView(generic.ListView):
    model = Rulertransition
    template_name = "crisisdb/rulertransition/rulertransition_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        return reverse('rulertransitions')


class RulertransitionDetailView(generic.DetailView):
    model = Rulertransition
    template_name = "crisisdb/rulertransition/rulertransition_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # form = RulertransitionForm
        # Add in a QuerySet of all the books
        # context["myform"] = form
        return context


class RulertransitionCreate(PermissionRequiredMixin, CreateView):
    model = Rulertransition
    form_class = RulertransitionForm
    template_name = "crisisdb/rulertransition/rulertransition_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('rulertransition-create')


class RulertransitionUpdate(PermissionRequiredMixin, UpdateView):
    model = Rulertransition
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    template_name = "crisisdb/rulertransition/rulertransition_form.html"
    permission_required = 'catalog.can_mark_returned'


class RulertransitionDelete(PermissionRequiredMixin, DeleteView):
    model = Rulertransition
    success_url = reverse_lazy('rulertransitions')
    permission_required = 'catalog.can_mark_returned'


############# Agr Prod and Pop ########################

class Agr_Prod_PopListView(generic.ListView):
    model = Agr_Prod_Pop
    template_name = "crisisdb/Agr_Prod_Pop/agr_prod_pop_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        a_random_dic = {
            "ali": "Taghaviasl",
            "rashid": "Khazeiy",
        }
        myvar = {
            'file_name': 'Qing - Datasets.xls',
            'sheet_name': 'Qing Famine',
            'full_var_name': 'Famine Outbreak',
            'polity': 'CnQingE',
            'general_description': "UNAVAILABLE IN THE FILE",
            'data_source': ['https://clio-infra.eu/Indicators/LabourersRealWage.html', ],
        }
        # form = Agr_Prod_PopForm
        # Add in a QuerySet of all the books
        context["mydata"] = a_random_dic
        context["myvar"] = myvar
        print(context)
        return context

    def get_absolute_url(self):
        return reverse('Agr_Prod_Pops')


class Agr_Prod_PopDetailView(generic.DetailView):
    model = Agr_Prod_Pop
    template_name = "crisisdb/Agr_Prod_Pop/agr_prod_pop_detail.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     a_random_dic = {
    #         "ali": "Taghaviasl",
    #         "rashid": "Khazeiy",
    #     }
    #     #form = Agr_Prod_PopForm
    #     # Add in a QuerySet of all the books
    #     context["myform"] = a_random_dic
    #     print(context)
    #     return context


class Agr_Prod_PopCreate(PermissionRequiredMixin, CreateView):
    model = Agr_Prod_Pop
    form_class = Agr_Prod_PopForm
    template_name = "crisisdb/Agr_Prod_Pop/agr_prod_pop_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # form = RulertransitionForm
        # Add in a QuerySet of all the books
        context["icon1"] = mark_safe(
            '<i class="fas fa-tractor float-end fa-3x"></i>')
        context["icon2"] = mark_safe(
            '<i class="fas fa-seedling float-end fa-3x"></i>')
        return context

    def get_absolute_url(self):
        return reverse('Agr_Prod_Pop-create')


class Agr_Prod_PopUpdate(PermissionRequiredMixin, UpdateView):
    model = Agr_Prod_Pop
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    template_name = "crisisdb/Agr_Prod_Pop/agr_prod_pop_form.html"
    permission_required = 'catalog.can_mark_returned'


class Agr_Prod_PopDelete(PermissionRequiredMixin, DeleteView):
    model = Agr_Prod_Pop
    success_url = reverse_lazy('Agr_Prod_Pops')
    permission_required = 'catalog.can_mark_returned'


@permission_required('admin.can_add_log_entry')
def agr_prod_pop_download(request):
    items = Agr_Prod_Pop.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="allagrprodpods.csv"'

    writer = csv.writer(response, delimiter='|')
    # writer.writerow(['title', 'author',
    #                  'isbn', 'genre', 'language', ])
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_population', 'arable_land_per_capita'])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_population, obj.arable_land_per_capita])

    return response


# crisisdb vars

vars_dic = {
    'Agr_Prod_Pop_key': {
        'model': Agr_Prod_Pop,
        'list': Agr_Prod_PopListView,
        'create': Agr_Prod_PopCreate,
    },

    'Rulertransition_key': {
        'model': Rulertransition,
        'list': RulertransitionListView,
        'create': RulertransitionCreate,
    },
}


class CrisisDBVarsView(ListView):
    template_name = 'crisisdb_vars.html'
    model = Agr_Prod_Pop

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # form = RulertransitionForm
        # Add in a QuerySet of all the books
        mylist = []
        for k, v in vars_dic.items():
            inner_list = []
            inner_list.append(v['model'].objects.count())
            # print(v['model'].objects.count())
            # print('kkkkkkkkkkkkkkkkkkkkkkkkkk')
            l = v['list']()
            inner_list.append(l.get_absolute_url())
            l = v['create']()
            inner_list.append(l.get_absolute_url())
            inner_list.append(v['model'].objects.first().name)
            mylist.append(inner_list)

        context["mylist"] = mylist
        context["agrpod"] = Agr_Prod_Pop.objects.all()
        print(context['mylist'])
        return context
