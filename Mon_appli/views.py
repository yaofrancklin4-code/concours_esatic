from django.shortcuts import render

def home(request):
    return render(request, 'Mon_appli/home.html')

def inscription(request):
    return render(request, 'Mon_appli/page2.html')

def contact(request):
    return render(request, 'Mon_appli/page1.html')
