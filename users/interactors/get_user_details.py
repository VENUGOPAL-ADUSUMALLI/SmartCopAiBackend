from users.models import User
from django.core.exceptions import ObjectDoesNotExist

class GetUserDetailsInteractor:
    def __init__(self, phone_number):
        self.phone_number = phone_number
     

    def get_user_details(self):
        # Step 1: Verify OTP
        user_otp = User.objects.get(phone=self.phone_number)
        if user_otp.otp != 123456:
            return {
                "error": "Invalid OTP",
                "status": "failed"
            }

        # Step 2: Fetch user
        try:
            user = User.objects.get(phone=self.phone_number)
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
        except ObjectDoesNotExist:
            return {
                "error": "User not found",
                "status": "failed"
            }
