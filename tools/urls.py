from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('softwares/', views.SoftwareList.as_view()),
    path('softwares/<int:pk>/', views.SoftwareDetail.as_view()),
    path('hardwares/', views.HardwareList.as_view()),
    path('hardwares/<int:pk>/', views.HardwareDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)