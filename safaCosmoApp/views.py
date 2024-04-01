from django.shortcuts import render

# Create your views here.

def go_to_home_page(request):
    return render(request, "home.html")
