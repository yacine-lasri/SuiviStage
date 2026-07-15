from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Etudiant, Stage
from .forms import EtudiantForm, StageForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EtudiantSerializer

# ─── Etudiant CRUD ────────────────────────────────────────────────

class EtudiantListView(LoginRequiredMixin, ListView):
    model = Etudiant
    template_name = 'etudiants/etudiant_list.html'
    context_object_name = 'etudiants'
    
    def get_queryset(self):
        user = self.request.user
        
        # Admins, Supervisors, and Companies can see the list of all students
        if user.is_superuser or user.role in ['SUPERVISOR', 'COMPANY']:
            return Etudiant.objects.all()
            
        # A student can ONLY see their own profile in the list
        if user.role == 'STUDENT':
            return Etudiant.objects.filter(email=user.email)
            
        return Etudiant.objects.none()


class EtudiantDetailView(LoginRequiredMixin, DetailView):
    model = Etudiant
    template_name = 'etudiants/etudiant_detail.html'
    context_object_name = 'etudiant'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        etudiant = self.object
        ctx['stages'] = etudiant.stages.select_related('entreprise').all()
        return ctx


class EtudiantCreateView(LoginRequiredMixin, CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'etudiants/etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')


class EtudiantUpdateView(LoginRequiredMixin, UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'etudiants/etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')


class EtudiantDeleteView(LoginRequiredMixin, DeleteView):
    model = Etudiant
    template_name = 'etudiants/etudiant_confirm_delete.html'
    success_url = reverse_lazy('etudiant_list')


# ─── Stage CRUD ───────────────────────────────────────────────────

class StageListView(LoginRequiredMixin, ListView):
    model = Stage
    template_name = 'etudiants/stage_list.html'
    context_object_name = 'stages'

    def get_queryset(self):
        user = self.request.user
        base_qs = Stage.objects.select_related('etudiant', 'entreprise')

        # 1. Admins see absolutely everything (including unassigned orphans)
        if user.is_superuser:
            return base_qs.all()

        # 2. Supervisors ONLY see stages assigned to them via the bridge table
        if user.role == 'SUPERVISOR':
            return base_qs.filter(encadrements__encadrant=user).distinct()

        # 3. Students only see their own stages (matched by email)
        if user.role == 'STUDENT':
            return base_qs.filter(etudiant__email=user.email)

        # 4. Company users only see stages hosted at their company
        if user.role == 'COMPANY':
            return base_qs.filter(entreprise__email=user.email)

        # Fallback: return nothing for unrecognised roles
        return base_qs.none()


class StageDetailView(LoginRequiredMixin, DetailView):
    model = Stage
    template_name = 'etudiants/stage_detail.html'
    context_object_name = 'stage'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        stage = self.object
        ctx['encadrements'] = stage.encadrements.select_related('encadrant').all()
        ctx['evaluations'] = stage.evaluations.all()
        ctx['rapports'] = stage.rapports.all()
        return ctx


class StageCreateView(LoginRequiredMixin, CreateView):
    model = Stage
    form_class = StageForm
    template_name = 'etudiants/stage_form.html'
    success_url = reverse_lazy('stage_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class StageUpdateView(LoginRequiredMixin, UpdateView):
    model = Stage
    form_class = StageForm
    template_name = 'etudiants/stage_form.html'
    success_url = reverse_lazy('stage_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class StageDeleteView(LoginRequiredMixin, DeleteView):
    model = Stage
    template_name = 'etudiants/stage_confirm_delete.html'
    success_url = reverse_lazy('stage_list')


# ─── API Views ────────────────────────────────────────────────────

class EtudiantListAPI(APIView):
    def get(self, request):
        etudiants = Etudiant.objects.all()
        serializer = EtudiantSerializer(etudiants, many=True)
        return Response(serializer.data)


class EtudiantDetailAPI(APIView):
    def get(self, request, pk):
        etudiant = Etudiant.objects.get(id=pk)
        serializer = EtudiantSerializer(etudiant, many=False)
        return Response(serializer.data)