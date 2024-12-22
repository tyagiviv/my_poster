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
    is_favorite = Favorite.objects.filter(poster_id_id=poster.id).exists()

    # Debugging: Print the value of is_favorite
    print(f"Is favorite: {is_favorite}")

    if request.method == 'POST':
        if is_favorite:
            # Remove favorites
            favorite = Favorite.objects.get(poster_id_id=poster.id)
            favorite.delete()
            return redirect('favorite')
        else:
            # Add favorites
            Favorite.objects.create(poster_id_id=poster.id)
            return redirect('favorite')



    return render(request, 'poster_details.html', {'poster': poster, 'is_favorite': is_favorite})