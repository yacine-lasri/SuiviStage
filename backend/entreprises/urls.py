from django.urls import path
from .views import (
    EntrepriseListView, EntrepriseDetailView,
    EntrepriseCreateView, EntrepriseUpdateView, EntrepriseDeleteView,
)

urlpatterns = [
    path('', EntrepriseListView.as_view(), name='entreprise_list'),
    path('<int:pk>/', EntrepriseDetailView.as_view(), name='entreprise_detail'),
    path('ajouter/', EntrepriseCreateView.as_view(), name='entreprise_create'),
    path('<int:pk>/modifier/', EntrepriseUpdateView.as_view(), name='entreprise_update'),
    path('<int:pk>/supprimer/', EntrepriseDeleteView.as_view(), name='entreprise_delete'),
]