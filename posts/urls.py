from cmath import exp
from django.urls import path 
from .views import MainView , export



app_name = 'posts'

urlpatterns = [
    path('' , MainView.as_view() , name='main'),
    path('<str:format>/' , export , name='export'),
]
