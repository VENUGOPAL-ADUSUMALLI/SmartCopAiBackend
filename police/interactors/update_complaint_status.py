from users.models import Complaint
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import uuid

class UpdateComplaintStatusInteractor:
    def __init__(self, complaint_id, new_status):
        self.complaint_id = complaint_id
        self.new_status = new_status

    def execute(self):
        try:
            # Validate UUID
            complaint_uuid = uuid.UUID(self.complaint_id)
        except ValueError:
            raise ValidationError("Invalid complaint ID format. Must be a UUID.")

        try:
            complaint = Complaint.objects.get(complaint_id=complaint_uuid)
        except ObjectDoesNotExist:
            raise ValidationError("Complaint not found.")

        valid_statuses = dict(Complaint.STATUS_CHOICES).keys()
        if self.new_status not in valid_statuses:
            raise ValidationError(f"Invalid status. Must be one of {list(valid_statuses)}")

        complaint.status = self.new_status
        complaint.save()

        return complaint
