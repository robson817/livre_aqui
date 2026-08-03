from django.urls import path

from . import views

app_name = 'ebook'
urlpatterns = [
    path('<uuid:id>/', views.ebook, name='ebook'),
    path('', views.ebook_search, name='ebook_search')
]