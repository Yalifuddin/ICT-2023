from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='itech'),
    path('daftar', views.daftar_view, name='daftar'),
    path('daftar/valorant', views.daftar_valorant_view, name='daftar-valorant'),
    path('daftar/shortmovie', views.daftar_short_movie_view,
         name='daftar-shortmovie'),
    path('daftar/poster', views.daftar_poster_view,
         name='daftar-poster'),
    path('daftar/valorant/sukses', views.daftarsuksesvalorant_view,
         name='daftar-sukses-valorant'),
    path('daftar/shortmovie/sukses', views.daftarsuksesshortmovie_view,
         name='daftar-sukses-shortmovie'),
    path('daftar/poster/sukses', views.daftarsuksesposter_view,
         name='daftar-sukses-poster'),
    path('about', views.about_view, name='about-itech'),
    path('juknis', views.juknis_view, name='juknis'),
    path('timeline', views.timeline_view, name='timeline'),
]
