# Generated by Django 4.2 on 2023-06-01 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_student_coursecode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='cousedate',
            new_name='coursedate',
        ),
    ]
