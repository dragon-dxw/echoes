from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world - this is the initial index view.")