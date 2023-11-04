from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404
import logging


def index(request):
    """
    Lettings page listing all Lettings objects in database
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Letting object detail page, called with object's id
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logging.error(f'Not existing Letting ID :{letting_id}')
        raise Http404
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
