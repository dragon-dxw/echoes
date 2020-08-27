from django.urls import path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('vision/<int:pk>/text', views.plain_text_vision, name="plain_text_vision")
]
