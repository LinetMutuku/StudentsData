# Generated by Django 5.0.4 on 2024-05-25 07:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_student_dob_alter_student_disabled_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="profile_pictire",
            new_name="profile_picture",
        ),
    ]
