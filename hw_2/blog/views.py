from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    data = []
    for a in articles:
        data.append({
            'id': a.id,
            'title': a.title,
            'text': a.text,
            'author': a.author
        })
    return JsonResponse(data, safe=False)

def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
        data = {
            'id': article.id,
            'title': article.title,
            'text': article.text,
            'author': article.author
        }
        return JsonResponse(data)
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)



# Create your views here.
