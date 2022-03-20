from django.shortcuts import render

# Create your views here.
def groups(request):
    return render(request, 'home.html')
