# Generated by Django 4.1 on 2023-02-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_solution_solution_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='rejected_solution',
            field=models.BooleanField(default=False),
        ),
    ]
