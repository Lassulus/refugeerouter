from django.shortcuts import render

# Create your views here.
def group(request):
    return render(request, 'group.html')
