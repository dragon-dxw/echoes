from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from core.models import Vision, Volume

admin.site.register(Volume)

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    fields = ('volume', 'visionary', 'guide', 'dose_origin', 'account',
              'soul_status', 'ritual_results', 'commentary', 'plain_text_link',
              'ready_to_publish')
    readonly_fields = ('plain_text_link',)

    def plain_text_link(self, obj):
        return format_html("<a href='{plain}'>{plain}</a>", plain=reverse("plain_text_vision", args=(obj.pk,)))

    def get_fields(self, request, obj=None):
        """
        Modify get_fields() so that we only show plain_text_link on change pages, not add pages.
        Adapted from https://stackoverflow.com/questions/1245214/django-admin-exclude-field-on-change-form-only .
        Will need replacing if we move to using fieldsets rather than just fields in VisionAdmin.
        """
        fields = list(super(VisionAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if not obj:  # obj will be None on the add page, and something on change pages
            exclude_set.add('plain_text_link')
        return [f for f in fields if f not in exclude_set]
