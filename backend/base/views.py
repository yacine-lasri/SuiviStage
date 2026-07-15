from django.shortcuts import render
from django.views import View
from etudiants.models import Etudiant, Stage
from entreprises.models import Entreprise
from encadrement.models import Encadrement, Encadrant
from evaluations.models import Evaluation
from rapports.models import Rapport


class HomeView(View):
    def get(self, request):
        user = request.user

        # ── Not logged in → public landing page ──────────────
        if not user.is_authenticated:
            return render(request, 'base/home_public.html')

        # ── Admin (superuser) → full dashboard ───────────────
        if user.is_superuser:
            context = {
                'nb_etudiants':    Etudiant.objects.count(),
                'nb_stages':       Stage.objects.count(),
                'nb_entreprises':  Entreprise.objects.count(),
                # nb_encadrants  = count of supervisor PEOPLE (Encadrant profile rows)
                # nb_encadrements = count of stage ASSIGNMENTS (bridge table rows)
                # The dashboard card shows people, so we use nb_encadrants.
                'nb_encadrants':   Encadrant.objects.count(),
                'nb_encadrements': Encadrement.objects.count(),
                'nb_evaluations':  Evaluation.objects.count(),
                'nb_rapports':     Rapport.objects.count(),
                'stages_en_cours': Stage.objects.filter(statut='en_cours')
                    .select_related('etudiant', 'entreprise')[:5],
                'derniers_rapports': Rapport.objects.select_related('stage__etudiant')[:5],
                'dernieres_evaluations': Evaluation.objects.select_related('stage__etudiant')[:5],
            }
            return render(request, 'base/home_admin.html', context)

        # ── Student → their own stages, reports, evaluations ─
        if user.role == 'STUDENT':
            # Find stages where the student email matches the user email
            mes_stages = Stage.objects.filter(
                etudiant__email=user.email
            ).select_related('entreprise')
            stage_ids = mes_stages.values_list('id', flat=True)
            context = {
                'mes_stages': mes_stages,
                'nb_stages': mes_stages.count(),
                'mes_rapports': Rapport.objects.filter(stage_id__in=stage_ids)
                    .select_related('stage')[:5],
                'mes_evaluations': Evaluation.objects.filter(stage_id__in=stage_ids)
                    .select_related('stage')[:5],
                'nb_rapports': Rapport.objects.filter(stage_id__in=stage_ids).count(),
                'nb_evaluations': Evaluation.objects.filter(stage_id__in=stage_ids).count(),
            }
            return render(request, 'base/home_student.html', context)

        # ── Supervisor → ONLY stages explicitly assigned via Encadrement ────
        if user.role == 'SUPERVISOR':
            # Traverse the bridge table: Stage → Encadrement → encadrant FK
            # .distinct() prevents duplicate Stage rows when one stage has
            # multiple Encadrement records (e.g., academic + company supervisor).
            mes_stages = Stage.objects.filter(
                encadrements__encadrant=user
            ).select_related('etudiant', 'entreprise').distinct()

            stage_ids = mes_stages.values_list('id', flat=True)

            # Fetch the Encadrement rows themselves (for the dashboard card)
            mes_encadrements = Encadrement.objects.filter(
                encadrant=user
            ).select_related('stage__etudiant', 'stage__entreprise')

            context = {
                'mes_stages': mes_stages,
                'mes_encadrements': mes_encadrements,
                'nb_stages_supervises': mes_stages.count(),
                'evaluations': Evaluation.objects.filter(stage_id__in=stage_ids)
                    .select_related('stage__etudiant')[:5],
                'rapports': Rapport.objects.filter(stage_id__in=stage_ids)
                    .select_related('stage__etudiant')[:5],
                'nb_evaluations': Evaluation.objects.filter(stage_id__in=stage_ids).count(),
                'nb_rapports': Rapport.objects.filter(stage_id__in=stage_ids).count(),
            }
            return render(request, 'base/home_supervisor.html', context)


        # ── Company → stages hosted at their company ─────────
        if user.role == 'COMPANY':
            # Find entreprise matching the user's email
            entreprise = Entreprise.objects.filter(email=user.email).first()
            if entreprise:
                stages = Stage.objects.filter(
                    entreprise=entreprise
                ).select_related('etudiant')
            else:
                stages = Stage.objects.none()
            context = {
                'entreprise': entreprise,
                'stages': stages,
                'nb_stages': stages.count(),
                'nb_en_cours': stages.filter(statut='en_cours').count(),
                'nb_termines': stages.filter(statut='termine').count(),
            }
            return render(request, 'base/home_company.html', context)

        # Fallback
        return render(request, 'base/home_public.html')