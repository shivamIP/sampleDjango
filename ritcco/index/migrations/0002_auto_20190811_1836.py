# Generated by Django 2.2.3 on 2019-08-11 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='applicant_cv',
            new_name='cv',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='applicant_domain',
            new_name='domain',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='applicant_exp',
            new_name='exp',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='applicant_id',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='applicant_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='applicant_phone',
            new_name='phone',
        ),
    ]