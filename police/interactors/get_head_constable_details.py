from users.models import User
from police.models import OfficerRole

class GetHeadConstableDetailsByPhoneInteractor:
    def __init__(self, phone):
        self.phone = phone

    def execute(self):
        try:
            user = User.objects.get(phone=self.phone)
        except User.DoesNotExist:
            raise ValueError("User with this phone number not found.")

        try:
            role = OfficerRole.objects.get(officer=user)
        except OfficerRole.DoesNotExist:
            raise ValueError("This user is not assigned any police role.")

        if role.designation != 'head_constable':
            raise ValueError("This user is not a Head Constable.")

        # Default OTP check (198627)
        if user.otp != 198627:
            raise ValueError("Invalid OTP.")

        return {
            "user_id": str(user.user_id),
            "name": user.name,
            "phone": user.phone,
            "designation": role.get_designation_display(),
            "department": role.department or "Not Assigned"
        }
