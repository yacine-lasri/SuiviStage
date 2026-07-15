from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Evaluation
from .forms import EvaluationForm


class EvaluationListView(LoginRequiredMixin, ListView):
    model = Evaluation
    template_name = 'evaluations/evaluation_list.html'
    context_object_name = 'evaluations'

    def get_queryset(self):
        user = self.request.user
        base_qs = Evaluation.objects.select_related('stage__etudiant', 'stage__entreprise')

        if user.is_superuser or user.role == 'SUPERVISOR':
            return base_qs.all()

        if user.role == 'STUDENT':
            return base_qs.filter(stage__etudiant__email=user.email)

        if user.role == 'COMPANY':
            return base_qs.filter(stage__entreprise__email=user.email)

        return base_qs.none()


class EvaluationDetailView(LoginRequiredMixin, DetailView):
    model = Evaluation
    template_name = 'evaluations/evaluation_detail.html'
    context_object_name = 'evaluation'


class EvaluationCreateView(LoginRequiredMixin, CreateView):
    model = Evaluation
    form_class = EvaluationForm
    template_name = 'evaluations/evaluation_form.html'
    success_url = reverse_lazy('evaluation_list')

    def post(self, request, *args, **kwargs):
        """
        Explicit POST handler implementing the Post-Redirect-Get (PRG) pattern.

        Why override the generic CreateView.post()?
        The default implementation re-renders the form silently on validation
        failure with no user feedback. By overriding it we can:
          1. Show a flash success message via Django's messages framework.
          2. Show a descriptive flash error message listing what went wrong,
             so the teacher knows exactly which field failed validation.
          3. Guarantee a redirect after every successful save (PRG), which
             prevents duplicate submissions on browser refresh.
        """
        self.object = None  # Required by CreateView's internal machinery
        form = self.get_form()

        if form.is_valid():
            evaluation = form.save()
            messages.success(
                request,
                f"Évaluation enregistrée avec succès : {evaluation.note}/20 "
                f"pour {evaluation.stage.etudiant}."
            )
            return redirect(self.success_url)

        # Form is invalid — collect field-level errors into one readable message
        error_details = "; ".join(
            f"{field}: {', '.join(errs)}"
            for field, errs in form.errors.items()
        )
        messages.error(
            request,
            f"Échec de l'enregistrement. Veuillez corriger les erreurs : {error_details}"
        )
        # Re-render the form with validation errors visible (NOT a redirect)
        return self.form_invalid(form)


class EvaluationUpdateView(LoginRequiredMixin, UpdateView):
    model = Evaluation
    form_class = EvaluationForm
    template_name = 'evaluations/evaluation_form.html'
    success_url = reverse_lazy('evaluation_list')

    def post(self, request, *args, **kwargs):
        """
        Same PRG pattern as EvaluationCreateView, applied to updates.
        self.object must be fetched first so UpdateView machinery works.
        """
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            evaluation = form.save()
            messages.success(
                request,
                f"Évaluation mise à jour : {evaluation.note}/20 "
                f"pour {evaluation.stage.etudiant}."
            )
            return redirect(self.success_url)

        error_details = "; ".join(
            f"{field}: {', '.join(errs)}"
            for field, errs in form.errors.items()
        )
        messages.error(
            request,
            f"Échec de la mise à jour. Veuillez corriger : {error_details}"
        )
        return self.form_invalid(form)


class EvaluationDeleteView(LoginRequiredMixin, DeleteView):
    model = Evaluation
    template_name = 'evaluations/evaluation_confirm_delete.html'
    success_url = reverse_lazy('evaluation_list')

    def post(self, request, *args, **kwargs):
        evaluation = self.get_object()
        label = f"{evaluation.note}/20 pour {evaluation.stage.etudiant}"
        response = super().post(request, *args, **kwargs)
        messages.warning(request, f"Évaluation supprimée : {label}.")
        return response
