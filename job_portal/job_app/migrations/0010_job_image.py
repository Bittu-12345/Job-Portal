# Generated by Django 5.0 on 2024-07-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0009_remove_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]