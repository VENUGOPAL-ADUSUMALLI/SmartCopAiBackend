from users.models import Complaint
from django.core.exceptions import ObjectDoesNotExist

class GetUserComplaintsInteractor:
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        complaints = Complaint.objects.filter(user_id=self.user_id).select_related('case_type')
        return [{
            "complaint_id": str(comp.complaint_id),
            "case_type": comp.case_type.name,
            "status": comp.status,
            "incident_summary": comp.incident_summary,
            "incident_date": comp.incident_date
        } for comp in complaints]
