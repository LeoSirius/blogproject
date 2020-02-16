from django.contrib import admin
from django.urls import path

from doctree_server.views import home_view_for_react, github_callback
from doctree_server.api import DocTreeView

urlpatterns = [
    path('', home_view_for_react),

    path('github-callback', github_callback),
    path('admin/', admin.site.urls),


    # api
    path('api/doctree/', DocTreeView.as_view())
]
