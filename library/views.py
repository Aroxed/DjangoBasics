from django.http import JsonResponse, HttpResponse

from library.models import Book


def book_count(request):
    the_book_count = Book.objects.all().count()
    return JsonResponse({'book count': the_book_count})


def all_books(request):
    result = {}
    for book in Book.objects.all():
        result[book.id] = {"book_name": book.book_name, "pages": book.pages}
    return JsonResponse({'result': result})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    return HttpResponse(f"<h1>{book.book_name}</h1><p>{book.pages}</p>")
