## Admin

```python
from django.contrib import admin

```

## Apps

```python
from django.apps import AppConfig

class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.notification'

```

## Controllers

```python
# Controllers
```

## Models

```python
from django.db import models

class NotificationModel(models.Model):
    
    type_notification = models.CharField(max_length=255)
    message = models.TextField()
    datetime_notification = models.DateTimeField(auto_now_add=True)
    status_notification = models.BooleanField(default=False)
    
    #Foreign Keys
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type_notification
    
```

## Repository

```python
# Repository
```

## Schemas

```python
# Schemas 
```

## Services

```python

```

## Tests

```python
from django.test import TestCase

```

## __init__

```python

```

## 0001_initial

```python
# Generated by Django 5.1.4 on 2024-12-11 17:31

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
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_notification', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('datetime_notification', models.DateTimeField(auto_now_add=True)),
                ('status_notification', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```

## __init__

```python

```

