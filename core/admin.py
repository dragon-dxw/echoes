from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from core.models import Vision, Volume

admin.site.register(Volume)

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    fields = ('volume', 'visionary', 'guide', 'dose_origin', 'account',
              'soul_status', 'ritual_results', 'commentary', 'plain_text_link')
    readonly_fields = ('plain_text_link',)

    def plain_text_link(self, obj):
        return format_html("<a href='{plain}'>{plain}</a>", plain=reverse("plain_text_vision", args=(obj.pk,)))
