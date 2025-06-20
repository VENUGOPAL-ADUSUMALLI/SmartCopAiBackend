from users.models import User
from django.core.exceptions import ObjectDoesNotExist

class UpdateCurrentAddressInteractor:
    def __init__(self, phone_number, current_address):
        self.phone_number = phone_number
        self.current_address = current_address

    def update_current_address(self):
        try:
            user = User.objects.get(phone=self.phone_number)
            user.current_address = self.current_address
            user.save()

            return {
                "success": True,
                "message": "Current address updated successfully",
                "user_id": str(user.user_id),
                "current_address": user.current_address
            }
        except ObjectDoesNotExist:
            return {
                "success": False,
                "message": "User not found"
            }
