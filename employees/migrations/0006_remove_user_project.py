# Generated by Django 3.2.6 on 2021-08-03 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_user_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='project',
        ),
    ]
