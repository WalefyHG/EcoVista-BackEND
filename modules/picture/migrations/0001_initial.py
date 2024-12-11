# Generated by Django 5.1.4 on 2024-12-11 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biomes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('date_capture', models.DateField(blank=True, null=True)),
                ('localization_picture', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('biome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biomes.biomemodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]