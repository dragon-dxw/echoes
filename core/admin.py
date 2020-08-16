from django.contrib import admin

# Register your models here.
from core.models import Vision, Volume

admin.site.register(Volume)
admin.site.register(Vision)
