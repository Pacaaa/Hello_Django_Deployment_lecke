from django.shortcuts import render

# Create your views here.

def lap_betoltese(request):
    return render(request, 'lap.html')
