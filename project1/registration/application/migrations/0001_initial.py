# Generated by Django 5.0.2 on 2024-02-29 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('p_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=300)),
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
