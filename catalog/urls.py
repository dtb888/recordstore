from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('musicians/', views.MusicianListView.as_view(), name='musicians'),
    path('musician/<int:pk>', views.MusicianDetailView.as_view(), name='musician-detail'),
    
]
