from django.shortcuts import render
from django.http.response import JsonResponse


# Create your views here.
def home(request):
    return render(request, "index.html")


def books(request):
    books = [
        {'id': 1, 'title': 'Python', 'price': 89.00},
        {'id': 2, 'title': 'Django', 'price': 99.00},
        {'id': 3, 'title': 'Flask', 'price': 79.00},
    ]
    return JsonResponse(books, safe=False)
