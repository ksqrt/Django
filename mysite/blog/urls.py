from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('postlist', views.post_list, name='post_list'),

]
