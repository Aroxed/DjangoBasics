from django.contrib import admin
from django.urls import path, include
from .views import book_count, all_books, book_detail

urlpatterns = [
    path('book-count/', book_count),
    path('all_books/', all_books),
    path('book_detail/<int:book_id>', book_detail),
]