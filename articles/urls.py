
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<slug>/',views.article_detail, name='detail'),
    path('article/<int:pk>/comment/', views.add_comment_to_article, name='add_comment_to_article'),
]
