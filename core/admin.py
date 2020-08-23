from django.contrib import admin

# Register your models here.
from core.models import Vision, Volume

admin.site.register(Volume)

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    fields = ('volume', 'visionary', 'guide', 'dose_origin', 'account', 'ritual_results')
