import os

from django.shortcuts import render
from django.conf import settings





def home_view_for_react(request):








    return render(request, 'base_for_react.html')


def github_callback(request):
    """
    used to handle github webhooks, to auto pull notes repo
    """
    pass