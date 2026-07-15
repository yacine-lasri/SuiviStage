from django.urls import path
from .views import (
    EncadrementListView, EncadrementDetailView,
    EncadrementCreateView, EncadrementUpdateView, EncadrementDeleteView,
)

urlpatterns = [
    path('', EncadrementListView.as_view(), name='encadrement_list'),
    path('<int:pk>/', EncadrementDetailView.as_view(), name='encadrement_detail'),
    path('ajouter/', EncadrementCreateView.as_view(), name='encadrement_create'),
    path('<int:pk>/modifier/', EncadrementUpdateView.as_view(), name='encadrement_update'),
    path('<int:pk>/supprimer/', EncadrementDeleteView.as_view(), name='encadrement_delete'),
]