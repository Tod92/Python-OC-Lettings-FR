from django.contrib import admin
from django.urls import path, include

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
