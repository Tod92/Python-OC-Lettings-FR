from django.contrib import admin
from django.urls import path, include

from . import views
from lettings import views as lettings_views
from profiles import views as profiles_views

lettings_patterns = [
    path('', lettings_views.index, name='lettings_index'),
    path('<int:letting_id>/', lettings_views.letting, name='letting'),

]

profiles_patterns = [
    path('', profiles_views.index, name='profiles_index'),
    path('<str:username>/', profiles_views.profile, name='profile'),

]
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include(lettings_patterns)),
    path('profiles/', include(profiles_patterns))

]
