from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Book, Category


class HomeView(TemplateView):
    template_name = 'home.html'


def read_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'read_book.html', {'book': book})


def read_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'read_book.html', {'book': book})


def read_online(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'read_online.html', {'book': book})




def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'home.html', context)


def home(request):
    category_id = request.GET.get('category')
    if category_id:
        books = Book.objects.filter(book_category_id=category_id)
    else:
        books = Book.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'home.html', {'books': books, 'categories': categories})
    

