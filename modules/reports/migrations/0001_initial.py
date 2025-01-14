# Generated by Django 5.1.4 on 2024-12-11 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('picture', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_report', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_report', models.DateTimeField(auto_now_add=True)),
                ('status_report', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.commentsmodel')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picture.picturemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
