from profiles import views
from django.urls import path


profiles_patterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile')
]
