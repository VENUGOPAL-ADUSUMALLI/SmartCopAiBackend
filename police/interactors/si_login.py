from users.models import User
from police.models import OfficerRole

class SiLoginInteractor:
    def __init__(self, phone, otp):
        self.phone = phone
        self.otp = otp

    def execute(self):
        try:
            user = User.objects.get(phone=self.phone)
        except User.DoesNotExist:
            return {"status": "failed", "error": "User not found or not a Sub-Inspector"}

        if self.otp != 484382:
            return {"status": "failed", "error": "Invalid OTP"}

        try:
            role = OfficerRole.objects.get(officer=user)
            if role.designation != 'sub_inspector':
                return {"status": "failed", "error": "User not found or not a Sub-Inspector"}
        except OfficerRole.DoesNotExist:
            return {"status": "failed", "error": "User not found or not a Sub-Inspector"}

        return {
            "status": "success",
            "user_id": str(user.user_id),
            "name": user.name,
            "phone": user.phone,
            "designation": role.get_designation_display(),
            "department": role.department or "Not Assigned",
            "role_key": role.designation
        }
