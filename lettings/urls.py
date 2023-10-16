from lettings import views
from django.urls import path

lettings_patterns = [
    path('', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting')
]
