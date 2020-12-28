from django.urls import path
from Sale import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
