from django.db import models
from employees.models import Project, User

# Create your models here.
EQUIPMENT_TYPE_CHOICES = [
    ('HW', 'Hardware'),
    ('SW', 'Software')
]

EQUIPMENT_STATUS_CHOICES = [
    ('OBSOLETE', 'obsolete'),
    ('AVAILABLE', 'Available'),
    ('UNDER_REPAIR', 'Under repair'),
    ('SAMPLING', 'Sampling'),
    ('UNRELIABLE', 'Unreliable')
]

# Create your models here.
class Software(models.Model):
    type =  models.CharField(default=EQUIPMENT_TYPE_CHOICES[1][1], max_length=10)
    version = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=EQUIPMENT_STATUS_CHOICES, max_length=20)
    qa_reference = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    buy_date = models.DateField()
    details = models.TextField()

    def __str__(self) -> str:
        return self.designation


class Hardware(models.Model):
    type =  models.CharField(default=EQUIPMENT_TYPE_CHOICES[0][1], max_length=10)
    version = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=EQUIPMENT_STATUS_CHOICES, max_length=20)
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
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="updated_by")
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=DOCUMENT_STATUS_CHOICES, max_length=50)

    def __str__(self) -> str:
        return f'[{self.type}] {self.title}'

LANGUAGES_CHOICES = [
    ('C', 'C'),
    ('C++', 'C++'),
    ('C#', 'C#'),
    ('JAVA', 'Java'),
    ('RUBY', 'Ruby'),
    ('GOLANG', 'Golang')
]

class GenericFunction(models.Model):
    """
    Titre, Auteur, Date de création, Description, Date dernière Modification, Modifié par, Réviseur, 
    Etat (Brouillon, En Relecture, En cours de correction, publié), Mot clés, Langage, Projet
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=255)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="author")
    status = models.CharField(choices=DOCUMENT_STATUS_CHOICES, max_length=50)
    keywords = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGES_CHOICES, max_length=20)
    
    def __str__(self) -> str:
        return f'[{self.language}] {self.title}'