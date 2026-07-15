from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Encadrement


class EncadrementListView(LoginRequiredMixin, ListView):
    model = Encadrement
    template_name = 'encadrement/encadrement_list.html'
    context_object_name = 'encadrements'

    def get_queryset(self):
        user = self.request.user
        base_qs = Encadrement.objects.select_related(
            'stage__etudiant', 'stage__entreprise', 'encadrant'
        )

        # Admins see every assignment across all supervisors
        if user.is_superuser:
            return base_qs.all()

        # Supervisors see ONLY the assignments where they are the named encadrant.
        # Using encadrant=user (FK match) is stricter than encadrant_nom because
        # encadrant_nom is a free-text fallback — anyone could type any name there.
        if user.role == 'SUPERVISOR':
            return base_qs.filter(encadrant=user)

        # All other roles (STUDENT, COMPANY) have no business on this page.
        return base_qs.none()


class EncadrementDetailView(LoginRequiredMixin, DetailView):
    model = Encadrement
    template_name = 'encadrement/encadrement_detail.html'
    context_object_name = 'encadrement'


class EncadrementCreateView(LoginRequiredMixin, CreateView):
    model = Encadrement
    template_name = 'encadrement/encadrement_form.html'
    fields = ['stage', 'encadrant', 'encadrant_nom', 'role', 'date_debut', 'date_fin']
    success_url = reverse_lazy('encadrement_list')


class EncadrementUpdateView(LoginRequiredMixin, UpdateView):
    model = Encadrement
    template_name = 'encadrement/encadrement_form.html'
    fields = ['stage', 'encadrant', 'encadrant_nom', 'role', 'date_debut', 'date_fin']
    success_url = reverse_lazy('encadrement_list')


class EncadrementDeleteView(LoginRequiredMixin, DeleteView):
    model = Encadrement
    template_name = 'encadrement/encadrement_confirm_delete.html'
    success_url = reverse_lazy('encadrement_list')

