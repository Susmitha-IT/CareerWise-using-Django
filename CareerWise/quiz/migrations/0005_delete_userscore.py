# Generated by Django 5.0.2 on 2024-02-29 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_userscore'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserScore',
        ),
    ]
