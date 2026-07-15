from django.urls import path
from .views import (
    EtudiantListView, EtudiantDetailView,
    EtudiantCreateView, EtudiantUpdateView, EtudiantDeleteView,
    StageListView, StageDetailView,
    StageCreateView, StageUpdateView, StageDeleteView,
    EtudiantListAPI, EtudiantDetailAPI,
)

urlpatterns = [
    # Etudiants
    path('', EtudiantListView.as_view(), name='etudiant_list'),
    path('<int:pk>/', EtudiantDetailView.as_view(), name='etudiant_detail'),
    path('ajouter/', EtudiantCreateView.as_view(), name='etudiant_create'),
    path('<int:pk>/modifier/', EtudiantUpdateView.as_view(), name='etudiant_update'),
    path('<int:pk>/supprimer/', EtudiantDeleteView.as_view(), name='etudiant_delete'),
    # Stages
    path('stages/', StageListView.as_view(), name='stage_list'),
    path('stages/<int:pk>/', StageDetailView.as_view(), name='stage_detail'),
    path('stages/ajouter/', StageCreateView.as_view(), name='stage_create'),
    path('stages/<int:pk>/modifier/', StageUpdateView.as_view(), name='stage_update'),
    path('stages/<int:pk>/supprimer/', StageDeleteView.as_view(), name='stage_delete'),
    # API
    path('api/', EtudiantListAPI.as_view(), name='etudiant_list_api'),
    path('api/<int:pk>/', EtudiantDetailAPI.as_view(), name='etudiant_detail_api'),
]