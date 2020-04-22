
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.formaddsubject, name="add"),
    path('delete/<int:subid>', views.delsubject, name="delete"),
    path('post/', views.postaddsubject, name="postsub"),
]