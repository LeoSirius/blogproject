from django.contrib import admin
from django.urls import path

from doctree_server.views import home_view_for_react

urlpatterns = [
    path('', home_view_for_react),
    path('admin/', admin.site.urls),
]
