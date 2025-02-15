# Generated by Django 4.0.5 on 2022-06-19 07:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repositorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('html_url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(related_name='repositories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
