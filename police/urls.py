# police/urls.py

from django.urls import path
from police.views import *
urlpatterns = [
    path('hc/profile/', get_head_constable_profile_view),
    path('si/login/', si_login_view),
    path('si/profile/', get_si_profile_view),
    path('si/complaints/', get_all_complaints_view),
    path('si/complaints/<uuid:complaint_id>', get_complaint_details_si_view),
    path('si/assign-complaint/', assign_complaint_to_hc_view),
    path("complaint/mark_under_investigation/", mark_under_investigation_view),
    path("police/head_constables/", list_head_constables_view),
    path("update_complaint_status/v1", update_complaint_status_view),


]
