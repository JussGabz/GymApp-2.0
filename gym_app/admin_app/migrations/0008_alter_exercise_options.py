# Generated by Django 4.2 on 2024-07-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin_app", "0007_alter_exercise_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="exercise",
            options={"permissions": [("view_exercises", "Can view Exercise")]},
        ),
    ]
