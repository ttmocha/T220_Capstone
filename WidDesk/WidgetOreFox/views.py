from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello There!, You're using WidDesk.")
    
# Create your views here.
