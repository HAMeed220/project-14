from django.shortcuts import render

# Create your views here.
def ganesh(request):
    return render(request,'ganesh.html')

def shiva(request):
    return render(request,'shiva.html')