from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Rapport
from .forms import RapportForm


class RapportListView(ListView):
    model = Rapport
    template_name = 'rapports/rapport_list.html'
    context_object_name = 'rapports'

    def get_queryset(self):
        user = self.request.user
        base_qs = Rapport.objects.select_related('stage__etudiant')

        if user.is_superuser or user.role == 'SUPERVISOR':
            return base_qs.all()

        if user.role == 'STUDENT':
            return base_qs.filter(stage__etudiant__email=user.email)

        if user.role == 'COMPANY':
            return base_qs.filter(stage__entreprise__email=user.email)

        return base_qs.none()


class RapportDetailView(DetailView):
    model = Rapport
    template_name = 'rapports/rapport_detail.html'
    context_object_name = 'rapport'


class RapportCreateView(LoginRequiredMixin, CreateView):
    model = Rapport
    form_class = RapportForm
    template_name = 'rapports/rapport_form.html'
    success_url = reverse_lazy('rapport_list')


class RapportUpdateView(LoginRequiredMixin, UpdateView):
    model = Rapport
    form_class = RapportForm
    template_name = 'rapports/rapport_form.html'
    success_url = reverse_lazy('rapport_list')


class RapportDeleteView(LoginRequiredMixin, DeleteView):
    model = Rapport
    template_name = 'rapports/rapport_confirm_delete.html'
    success_url = reverse_lazy('rapport_list')
