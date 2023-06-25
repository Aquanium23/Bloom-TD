from django.urls import path, include
from .views import template_form

urlpatterns = [
    path('', template_form, name='template_form')
]
