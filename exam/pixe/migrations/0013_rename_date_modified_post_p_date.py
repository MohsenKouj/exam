# Generated by Django 3.2.4 on 2024-06-28 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixe', '0012_post_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_modified',
            new_name='p_date',
        ),
    ]
