from django.shortcuts import render
from renderer.models import Poster
from django.shortcuts import render, get_object_or_404


# Create your views here.
def poster_details(request, id):
    try:
        poster = Poster.objects.get(id=id)
    except Poster.DoesNotExist:
        return render(request, 'poster_details.html', {'message': 'Poster not found'})

    return render(request, 'poster_details.html', {'poster': poster})