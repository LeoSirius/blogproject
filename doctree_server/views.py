from django.shortcuts import render

def home_view_for_react(request):
    return render(request, 'base_for_react.html')