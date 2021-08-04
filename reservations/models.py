from django.db import models
from employees.models import User
from tools.models import Software, Hardware, EQUIPMENT_TYPE_CHOICES

# Create your models here.

RESERVATION_STATUS = [
    ('IN_PROGRESS', 'In progress'),
    ('VALIDATED', 'Validated'),
    ('POSTPONED', 'Postponed'),
    ('REJECTED', 'Rejected')
]

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment_type = models.CharField(choices=EQUIPMENT_TYPE_CHOICES, max_length=20)
    sw_equipment = models.ForeignKey(Software,on_delete=models.CASCADE, null=True)
    hw_equipment = models.ForeignKey(Hardware,on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(choices=RESERVATION_STATUS, default=('IN_PROGRESS', 'In progress'), max_length=30)