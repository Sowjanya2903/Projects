# Generated by Django 3.2.12 on 2024-03-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_uid_todoapp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
