# Generated by Django 3.2.6 on 2021-10-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_remove_reservation_sw_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'In progress'), ('VALIDATED', 'Validated'), ('POSTPONED', 'Postponed'), ('REJECTED', 'Rejected'), ('DELETED', 'Deleted')], default=('IN_PROGRESS', 'In progress'), max_length=30),
        ),
    ]
