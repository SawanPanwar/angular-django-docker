# Generated by Django 3.2.25 on 2024-07-08 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORSAPI', '0002_rename_login_id_user_loginid'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='sos_user',
        ),
    ]
