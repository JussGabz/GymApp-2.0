# Generated by Django 4.2 on 2024-07-25 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin_app", "0006_alter_exercise_name_alter_exercise_target_area_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="exercise",
            options={"permissions": [("view_exercises", "Can View Exercise")]},
        ),
    ]