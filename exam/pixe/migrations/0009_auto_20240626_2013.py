# Generated by Django 3.2.4 on 2024-06-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixe', '0008_alter_post_c_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_e',
        ),
        migrations.AlterField(
            model_name='post',
            name='c_view',
            field=models.IntegerField(default=0),
        ),
    ]
