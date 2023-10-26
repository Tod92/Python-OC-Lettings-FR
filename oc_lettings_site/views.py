"""
Django project's level views.
Contains site entry point and custom errors pages
"""
from django.shortcuts import render


def index(request):
    """
    Site entry point
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    View used to override default django html error 404 page
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    View used to override default django html error 500 page
    """
    return render(request, '500.html', status=500)
