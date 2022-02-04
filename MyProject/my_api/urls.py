from django.urls import path
# from . views import article_list, article_detail
from . views import ArticleAPIView, ArticleDetail

urlpatterns = [
    # path('article/', article_list, name='article'),
    path('article/', ArticleAPIView.as_view(), name='article'),
    # path('article/<int:pk>/', article_detail, name='article-detail'),
    path('article/<int:id>/', ArticleDetail.as_view(), name='article-detail'),
]
