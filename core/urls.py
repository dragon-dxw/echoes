from django.urls import path, re_path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('vision/<int:pk>/text', views.plain_text_vision, name="plain_text_vision"),
    path('vision/<int:pk>', views.rich_text_vision, name="rich_text_vision"),
    re_path('volume/(?P<volume_number>[1-9][0-9]*[a-d])/text', views.plain_text_single_volume,
            name="plain_text_single_volume"),
    path('volume/<int:volume_major_number>/text', views.plain_text_full_year,
         name="plain_text_full_year"),
    re_path('volume/(?P<volume_number>[1-9][0-9]*[a-d])', views.rich_text_single_volume,
            name="rich_text_single_volume"),
    path('volume/<int:volume_major_number>', views.rich_text_full_year,
         name="rich_text_full_year"),
]
