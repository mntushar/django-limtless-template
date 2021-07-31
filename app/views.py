from django.shortcuts import render


#home
def home(request):
    return render(request, 'index.html')
