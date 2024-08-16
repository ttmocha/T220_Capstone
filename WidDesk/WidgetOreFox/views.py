from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'WidgetOreFox/home.html')
def about(request):
    return render(request, 'WidgetOreFox/about.html')
def contact(request):
    return render(request, 'WidgetOreFox/contact.html')
#@def index(request):
  #  return HttpResponse("Hello There!, You're using WidDesk.")
    
# Create your views here.
