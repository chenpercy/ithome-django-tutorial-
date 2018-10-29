from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
	template_name = 'home.html'
def index(request):
	return HttpResponse("Hello, Django. Nice 2 meet u.")

def test(request):
	return render(request, 'vendor/test.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'registration/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'registration/register.html', context)
