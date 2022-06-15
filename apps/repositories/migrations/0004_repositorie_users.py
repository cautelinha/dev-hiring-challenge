# Generated by Django 4.0.5 on 2022-06-14 19:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repositories', '0003_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositorie',
            name='users',
            field=models.ManyToManyField(related_name='repositories', to=settings.AUTH_USER_MODEL),
        ),
    ]