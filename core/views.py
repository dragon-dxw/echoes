from django.http import HttpResponse

# Create your views here.
from core.models import Vision


def index(request):
    return HttpResponse("Hello world - this is the initial index view.")

def plain_text_vision(request, pk):
    vision = Vision.objects.get(pk=pk)
    return HttpResponse(bytes(vision.account, encoding="utf8"), content_type="text/plain")