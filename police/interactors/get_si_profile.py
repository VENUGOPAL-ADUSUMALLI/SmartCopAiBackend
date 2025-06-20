from users.models import User
from police.models import OfficerRole

class GetSiProfileInteractor:
    def __init__(self, phone):
        self.phone = phone

    def execute(self):
        try:
            user = User.objects.get(phone=self.phone)
        except User.DoesNotExist:
            raise ValueError("User not found")

        try:
            role = OfficerRole.objects.get(officer=user)
        except OfficerRole.DoesNotExist:
            raise ValueError("Police role not assigned")

        if role.designation != 'sub_inspector':
            raise ValueError("User is not a Sub-Inspector")

        return {
            "status": "success",
            "user_id": str(user.user_id),
            "name": user.name,
            "phone": user.phone,
            "designation": role.get_designation_display(),
            "department": role.department or "Not Assigned"
        }
