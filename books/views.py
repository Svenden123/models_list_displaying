from django.shortcuts import render
from .models import Book
import datetime


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def sort_books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()

    context = {'books': books}
    if pub_date:
        books = Book.objects.all().filter(pub_date=pub_date)
        all_dates = Book.objects.values_list('pub_date').order_by('pub_date')
        all_dates_list = list()
        for i in all_dates:
            all_dates_list.append(i[0])
        pub_date_index = all_dates_list.index(datetime.datetime.strptime(pub_date, '%Y-%m-%d').date())
        prev_page = all_dates_list[pub_date_index-1] if pub_date_index != 0 else None
        next_page = all_dates_list[pub_date_index+1] if pub_date_index < len(all_dates_list) - 1 else None
        if prev_page:
            context['prev_page'] = prev_page.strftime('%Y-%m-%d')
        if next_page:
            context['next_page'] = next_page.strftime('%Y-%m-%d')
        context['books'] = books
    return render(request, template, context)
