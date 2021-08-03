from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="AES Tooling API",
      default_version='v1',
      description="Private RestAPI used for managing employees, users, projects, docs, software and hardware tools",
      terms_of_service="http://localhost:8000/api/employees/doc/",
      contact=openapi.Contact(email="contact@aes.org"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('users/', views.UserList.as_view(), name='users'),
   path('users/<int:pk>/', views.UserDetail.as_view()),
   path('projects/', views.ProjectList.as_view()),
   path('projects/<int:pk>/', views.ProjectDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)