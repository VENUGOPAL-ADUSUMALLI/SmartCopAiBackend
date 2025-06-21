from users.models import User
from police.models import OfficerRole

class ListHeadConstablesInteractor:
    def __init__(self, si_phone):
        self.si_phone = si_phone

    def execute(self):
        try:
            si_user = User.objects.get(phone=self.si_phone)
            si_role = OfficerRole.objects.get(officer=si_user, designation='sub_inspector')
        except (User.DoesNotExist, OfficerRole.DoesNotExist):
            raise ValueError("SI not found or role mismatch")

        # Filter Head Constables in same department as SI
        head_constables = OfficerRole.objects.filter(
            designation='head_constable',
            department=si_role.department
        ).select_related("officer")

        return {
            "status": "success",
            "head_constables": [
                {
                    "user_id": str(role.officer.user_id),
                    "name": role.officer.name,
                    "phone": role.officer.phone,
                    "department": role.department
                }
                for role in head_constables
            ]
        }
