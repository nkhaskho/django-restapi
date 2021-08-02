from django.db import models

# Create your models here.
TOOLS_TYPE_CHOICES = [
    ('HW', 'Hardware'),
    ('SW', 'Software')
]

STATUS_CHOICES = [
    ('STATE 1', 'State 1'),
    ('STATE 2', 'State 2'),
    ('STATE 3', 'State 3')
]

# Create your models here.

class Software(models.Model):
    type =  models.CharField(default=TOOLS_TYPE_CHOICES[1][1], max_length=10)
    version = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    qa_reference = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    buy_date = models.DateField()
    details = models.TextField()

    def __str__(self) -> str:
        return self.designation


class Hardware(models.Model):
    type =  models.CharField(default=TOOLS_TYPE_CHOICES[0][1], max_length=10)
    version = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    comptability = models.CharField(max_length=50)
    licence = models.CharField(max_length=100)
    drivers = models.CharField(max_length=255)
    link = models.CharField(max_length=2500)

    def __str__(self) -> str:
        return self.designation