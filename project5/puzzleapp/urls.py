from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('puzzle/', views.puzzle, name='puzzle'),
    path('guess/', views.guess, name='guess'),
]