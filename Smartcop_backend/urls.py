"""
URL configuration for Smartcop_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_user_deatils/v1',get_user_details),
    path('create_case_type/v1',create_case_type_view),
    path('create_current_address/v1',update_current_address_view),
    path('api_ai_assessment/v1', ai_assessment_view),
    path('create_complaint/v1',create_complaint_view),
    path('complaint/<uuid:complaint_id>/', get_complaint_details_view),
    path("create_non_cogniazable_case/v1",create_non_cognizable_complaint_view),
    path('user/complaints/<uuid:user_id>/',list_user_complaints)
]
