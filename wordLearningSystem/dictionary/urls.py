from django.urls import path
from . import views


app_name = 'dictionary'
urlpatterns = [
    path('<str:word>/', views.index, name='index'),
    path('my_list', views.myList, name='myList')
]