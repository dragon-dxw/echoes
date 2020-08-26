from django.http import HttpResponse

# Create your views here.
from django.template.response import SimpleTemplateResponse

from core.models import Vision


def index(request):
    return HttpResponse("Hello world - this is the initial index view.")

def plain_text_vision(request, pk):
    vision = Vision.objects.get(pk=pk)
    return SimpleTemplateResponse(template="plain_text_vision.txt", context={"vision": vision},
                                  content_type="text/plain")