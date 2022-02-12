from django.db.models.base import Model
#from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, response
from .models import Book, Author, BookInstance, Genre, Language, Quote

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from catalog.forms import RenewBookForm, BookForm


def index(request):
    """View function for home page of website (at ..../catalog/"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()
    num_languages = Language.objects.count()
    num_genres = Genre.objects.count()
    my_obj = Quote.objects.order_by('?')[0]
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'rand_q': my_obj,
        'xyz': my_obj.owner_real,
        'random_quote': Quote.objects.order_by('?')[0],
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_languages': num_languages,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

    # return HttpResponse('Hi there...')
# Create your views here.


class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['rand_q'] = Quote.objects.order_by('?')[0]
        #context['rand_q'] = my_obj
        #context['rand_q_pic'] = my_obj.owner_real.pic.url
        return context
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__contains = 'war')[:5]
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_queryset(self):
    #    return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_new_data'] = 'this is some data to be used in book_list.html Tempalte'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['rand_q'] = Quote.objects.order_by('?')[0]
        return context


class AuthorListView(generic.ListView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['rand_q'] = Quote.objects.order_by('?')[0]
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['rand_q'] = Quote.objects.order_by('?')[0]
        return context


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view forfor listing on loan books"""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('catalog.can_renew', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('all-borrowed'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/6/2020'}
    permission_required = 'catalog.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    #fields = '__all__'
    #initial = {'date_of_death': '11/6/2020'}
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    # Not recommended (potential security issue if more fields added)
    #fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_mark_returned'


@permission_required('admin.can_add_log_entry')
def book_download(request):
    items = Book.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="allbooks.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['title', 'author',
                     'isbn', 'genre', 'language', ])

    for obj in items:
        if('Comedy' in obj.display_genre()):
            writer.writerow([obj.title, obj.author,
                             obj.isbn, obj.display_genre(), obj.language])

    return response
