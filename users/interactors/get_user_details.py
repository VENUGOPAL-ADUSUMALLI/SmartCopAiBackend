from users.models import User
from django.core.exceptions import ObjectDoesNotExist

class GetUserDetailsInteractor:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def execute(self):
        try:
            user = User.objects.get(phone=self.phone_number)
        except User.DoesNotExist:
            return {
                "error": "User not found",
                "status": "failed"
            }

        # ✅ Step 1: Check default OTP
        if user.otp != 211213:
            return {
                "error": "Invalid OTP",
                "status": "failed"
            }

        # ✅ Step 2: Return user details
        return {
            "user_id": str(user.user_id),
            "name": user.name,
            "gender": user.gender,
            "dob": str(user.dob),
            "aadhar_number": user.aadhar_number,
            "phone": user.phone,
            "email": user.email,
            "permanent_address": user.permanent_address,
            "role": user.role,
            "created_at": user.created_at.isoformat(),
            "status": "success"
        }
