from django.db import models
from employees.models import User

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


DOCUMENT_TYPE_CHOICES = [
    ('GUIDE', 'Guide'),
    ('MEMO', 'Memo')
]

DOCUMENT_STATUS_CHOICES = [
    ('DRAFT', 'Draft'),
    ('IN_PROOFREADING', 'In proofreading'),
    ('IN_CORRECTION', 'In correction'),
    ('PUBLISHED', 'Published')
]

class Document(models.Model):
    type =  models.CharField(choices=DOCUMENT_TYPE_CHOICES, max_length=10)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=DOCUMENT_STATUS_CHOICES, max_length=50)

    def __str__(self) -> str:
        return f'[{self.type}] {self.title}'