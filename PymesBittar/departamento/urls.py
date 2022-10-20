from django.urls import path
from . import views

urlpatterns = [
    path('',views.departamento_views, name = 'departamento'),
]