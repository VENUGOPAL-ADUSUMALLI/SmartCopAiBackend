# Smartcop_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # All police-related APIs
    path('', include('police.urls')),

    # All user-related APIs
    path('get_user_deatils/v1', get_user_details),
    path('create_case_type/v1', create_case_type_view),
    path('create_current_address/v1', update_current_address_view),
    path('api_ai_assessment/v1', ai_assessment_view),
    path('create_complaint/v1', create_complaint_view),
    path('complaint/<uuid:complaint_id>/', get_complaint_details_view),
    path("create_non_cogniazable_case/v1", create_non_cognizable_complaint_view),
    path('user/complaints/<uuid:user_id>/', list_user_complaints),
]
