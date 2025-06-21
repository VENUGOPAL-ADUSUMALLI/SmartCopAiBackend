from users.models import Complaint
from police.models import *  

class ListAllComplaintsInteractor:
    def execute(self):
        complaints = Complaint.objects.all().select_related('user', 'case_type')
        data = []

        for complaint in complaints:
            latest_stage = complaint.progress_updates.last().get_stage_display() if complaint.progress_updates.exists() else "Not Started"

            data.append({
                "complaint_id": str(complaint.complaint_id),
                "user": {
                    "name": complaint.user.name,
                    "phone": complaint.user.phone
                },
                "case_type": complaint.case_type.name if complaint.case_type else "Unknown",
                "status": complaint.status,
                "current_stage": latest_stage,
                "created_at": complaint.created_at.isoformat()
            })

        return {
            "status": "success",
            "complaints": data
        }
