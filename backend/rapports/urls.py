from django.urls import path
from .views import (
    RapportListView, RapportDetailView,
    RapportCreateView, RapportUpdateView, RapportDeleteView,
)

urlpatterns = [
    path('', RapportListView.as_view(), name='rapport_list'),
    path('<int:pk>/', RapportDetailView.as_view(), name='rapport_detail'),
    path('ajouter/', RapportCreateView.as_view(), name='rapport_create'),
    path('<int:pk>/modifier/', RapportUpdateView.as_view(), name='rapport_update'),
    path('<int:pk>/supprimer/', RapportDeleteView.as_view(), name='rapport_delete'),
]