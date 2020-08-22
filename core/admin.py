from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin

# Register your models here.
from core.models import Vision, Volume

admin.site.register(Volume)
admin.site.register(Vision)
