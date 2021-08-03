

### Clone the project directory
Clone the project repository
```bat
git clone https://github.com/naiim-khaskhoussi/django-restapi.git
```

### Project Dependencies
**Installing requirements packages**
```bat
pip install -r requirements.txt
```

### User management
Use default admin superuser username: '**admin**' and password: '**Aes2021\*\***'

**Or create new admin superuser**
```bat
python manage.py createsuperuser
```

### Database migration
**Make migrations**
```bat
python manage.py makemigrations <app-name>
```
**Migrations**
```bat
python manage.py migrate
```

### Running the api
```bat
python manage.py runserver
```