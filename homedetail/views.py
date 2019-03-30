from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'homedetail/profile.html', args)


def index(request):
    """View function for home page of site."""

    # number of employer
    user_count = User.objects.all().count()

    context = {
        'user_count': user_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


