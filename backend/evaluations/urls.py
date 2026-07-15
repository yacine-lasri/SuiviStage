from django.urls import path
from .views import (
    EvaluationListView, EvaluationDetailView,
    EvaluationCreateView, EvaluationUpdateView, EvaluationDeleteView,
)

urlpatterns = [
    path('', EvaluationListView.as_view(), name='evaluation_list'),
    path('<int:pk>/', EvaluationDetailView.as_view(), name='evaluation_detail'),
    path('ajouter/', EvaluationCreateView.as_view(), name='evaluation_create'),
    path('<int:pk>/modifier/', EvaluationUpdateView.as_view(), name='evaluation_update'),
    path('<int:pk>/supprimer/', EvaluationDeleteView.as_view(), name='evaluation_delete'),
]