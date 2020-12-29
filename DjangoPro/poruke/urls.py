from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='poruke_index'),
    path('int/<int:broj>', views.number, name='poruke_broj'),
    path('int/', views.number, name='poruke_broj'),
    path('rec/<str:rec>', views.word, name='poruke_rec'),
    path('routes/', views.params, name='poruke_params'),
    path('hello/' , views.hello , name= 'poruke_hello')
]
