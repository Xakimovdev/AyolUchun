# Generated by Django 4.2.7 on 2024-01-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0004_alter_coursevideos_course"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursevideos",
            name="video",
            field=models.FileField(default=1, upload_to="course-videos"),
            preserve_default=False,
        ),
    ]
