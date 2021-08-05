from django.shortcuts import render
from .models import modmanager
# Create your views here.
def home(request):
    data = modmanager.morelation.all()
    return render(request,'home.html',{'data':data})
