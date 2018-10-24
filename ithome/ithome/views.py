from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
	return HttpResponse("Hello, Django. Nice 2 meet u.")

def test(request):
	return render(request, 'vendor/test.html')
