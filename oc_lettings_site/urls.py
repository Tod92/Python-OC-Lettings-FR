"""
Contains Django project's routes.
App's routes imported here. See app_name/urls.py
Overriding default 404 and 500 errors pages
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from lettings.urls import lettings_patterns
from profiles.urls import profiles_patterns


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include(lettings_patterns)),
    path('profiles/', include(profiles_patterns))
]

handler404 = 'oc_lettings_site.views.custom_404'

handler500 = 'oc_lettings_site.views.custom_500'
