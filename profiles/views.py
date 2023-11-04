from django.shortcuts import render
from profiles.models import Profile
from django.http import Http404
import logging


def index(request):
    """
    Profiles page listing all Profiles objects in database
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Profile object detail page, called with object's id
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logging.error(f'Not existing Profile name :{username}')
        raise Http404
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
