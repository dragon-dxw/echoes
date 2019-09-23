from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin

# Register your models here.
from .models import Person, SummitDate, WriteupSection, Vision

class VisionAdmin(ReverseModelAdmin):
    inline_type = 'tabular'
    inline_reverse = ['visionary',
                      'guide',
                      'date']

admin.site.register(Vision, VisionAdmin)