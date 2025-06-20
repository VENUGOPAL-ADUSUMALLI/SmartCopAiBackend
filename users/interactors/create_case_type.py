from users.models import CaseType
from django.core.exceptions import ObjectDoesNotExist

class CreateCaseTypeInteractor:
    def create_case_type(self, name):
        try:
            case_type = CaseType.objects.get(name=name)
            return case_type
        except ObjectDoesNotExist:
            case_type = CaseType.objects.create(name=name)
            return case_type
