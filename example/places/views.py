# Create your views here.

from django.shortcuts import render_to_response

from example.places.models import Place


def index(request):
    return render_to_response(
        'places/index.html',
        {
            'places': Place.objects.all(),
        }
    )
