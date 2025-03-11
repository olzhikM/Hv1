from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    # Извлекаем все объекты Movie
    movies = Movie.objects.all()
    # Превратим QuerySet в список словарей
    data = []
    for m in movies:
        data.append({
            'id': m.id,
            'title': m.title,
            'description': m.description,
            'producer': m.producer,
            'duration': m.duration
        })
    return JsonResponse(data, safe=False)

def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        data = {
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'producer': movie.producer,
            'duration': movie.duration
        }
        return JsonResponse(data)
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)


# Create your views here.
