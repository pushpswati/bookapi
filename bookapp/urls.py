from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/external-books', views.Bookview.as_view()),
    path('api/v1/books', views.BookDetailsview.as_view()),
    path('api/v1/books/<int:pk>/', views.BookDetailsview.as_view()),
    path('api/v1/books/<int:pk>/update', views.BookDetailsview.as_view()),

]
# http://localhost:8080/api/external-books?name=:nameOfABook

urlpatterns = format_suffix_patterns(urlpatterns)