# Generated by Django 4.2.17 on 2024-12-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_fileid_uploaded_file_file_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaded_file',
            name='date',
        ),
        migrations.AddField(
            model_name='uploaded_file',
            name='file_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
