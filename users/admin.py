from django.contrib import admin
from .models import User, CaseType, Complaint, AIAssessment, Accused, Evidence, Witness, ChatQuery
# Register your models here.
admin.site.register(User)
admin.site.register(CaseType)
admin.site.register(Complaint)
admin.site.register(AIAssessment)
admin.site.register(Accused)
admin.site.register(Evidence)
admin.site.register(Witness)
admin.site.register(ChatQuery)
