from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm, FoodForm
# Create your views here.
def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    # print(vendor_list)
    return render(request, 'vendors/vendor_detail.html', context)

def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VendorForm()
        # return redirect('/vendor/')
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)

def food_create_view(request):
    form = FoodForm(request.POST or None)
    context = {
        'form' : form
    }
    return render(request, "vendors/food_create.html", context)
