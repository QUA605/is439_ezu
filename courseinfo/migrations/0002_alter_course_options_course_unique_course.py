# Generated by Django 4.1.7 on 2023-02-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courseinfo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"ordering": ["course_number", "course_name"]},
        ),
        migrations.AddConstraint(
            model_name="course",
            constraint=models.UniqueConstraint(
                fields=("course_number", "course_name"), name="unique_course"
            ),
        ),
    ]
