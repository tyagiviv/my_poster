from django.shortcuts import render
from renderer.models import Poster
from django.shortcuts import render, get_object_or_404, redirect
from renderer.models import Poster, Favorite


# Create your views here.
def poster_details(request, id):
    try:
        poster = Poster.objects.get(id=id)
    except Poster.DoesNotExist:
        return render(request, 'poster_details.html', {'message': 'Poster not found'})

    # Adding section to check if poster is already fav or not and based on that show button add to fav
    is_favorite = False
    try:
        Favorite.objects.get(poster_id_id=poster)
        is_favorite = True
    except Favorite.DoesNotExist:
        is_favorite = False


    if request.method == 'POST':
        try:
            favorite = Favorite.objects.get(poster_id_id=poster.id)

        except Favorite.DoesNotExist:
            Favorite.objects.create(poster_id_id=poster.id)

        return redirect('favorite')


    return render(request, 'poster_details.html', {'poster': poster})