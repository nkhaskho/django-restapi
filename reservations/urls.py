from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="AES Tooling Reservations API",
      default_version='v1',
      description="Private RestAPI used for managing employees, users, projects, docs, software and hardware tools",
      terms_of_service="http://localhost:8000/api/reservations/doc/",
      contact=openapi.Contact(email="contact@aes.org"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('<int:pk>/', views.ReservationDetail.as_view(), name='reservation_details'),
   path('', views.ReservationList.as_view(), name='reservations_list'),
]


urlpatterns = format_suffix_patterns(urlpatterns)