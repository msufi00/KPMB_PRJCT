# Generated by Django 4.2 on 2023-04-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('studentname', models.TextField(max_length=128)),
                ('studentphone', models.CharField(max_length=20)),
                ('mentorname', models.TextField(max_length=128)),
                ('studentcourse', models.CharField(max_length=128)),
            ],
        ),
    ]