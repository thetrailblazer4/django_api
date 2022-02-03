from django.shortcuts import render
from . models import Article
from . serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.


def article_list(request):
	if request.method == 'GET':
		articles =Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return JsonResponse(serializer.data, safe=False)

