from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello world - this is the initial index view.")

class Example(TemplateView):
    template_name = 'example.html'
