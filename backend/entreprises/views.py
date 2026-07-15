from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Entreprise
from .forms import EntrepriseForm


class EntrepriseListView(ListView):
    model = Entreprise
    template_name = 'entreprises/entreprise_list.html'
    context_object_name = 'entreprises'


class EntrepriseDetailView(DetailView):
    model = Entreprise
    template_name = 'entreprises/entreprise_detail.html'
    context_object_name = 'entreprise'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['stages'] = self.object.stages.select_related('etudiant').all()
        return ctx


class EntrepriseCreateView(LoginRequiredMixin, CreateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = 'entreprises/entreprise_form.html'
    success_url = reverse_lazy('entreprise_list')


class EntrepriseUpdateView(LoginRequiredMixin, UpdateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = 'entreprises/entreprise_form.html'
    success_url = reverse_lazy('entreprise_list')


class EntrepriseDeleteView(LoginRequiredMixin, DeleteView):
    model = Entreprise
    template_name = 'entreprises/entreprise_confirm_delete.html'
    success_url = reverse_lazy('entreprise_list')
