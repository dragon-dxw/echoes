from django.urls import path, re_path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('vision/<int:pk>/text', views.plain_text_vision, name="plain_text_vision"),
    re_path('volume/(?P<volume_number>[1-9][0-9]*[a-d])/text', views.plain_text_single_volume,
            name="plain_test_single_volume"),
]
