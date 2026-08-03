from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
    path('<uuid:id>/', views.movie, name='movie'),
    path('', views.movie_search, name='movie_search')
]