from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^employees/$', views.employee_list),
    url(r'^employees/$', views.EmployeeList.as_view()),
]