## Admin

```python
from django.contrib import admin

```

## Apps

```python
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.users'

```

## Controllers

```python
from modules.users.models import User
from ninja_extra import api_controller, route
from modules.users.services import Services
from modules.users.schemas import UserListSchema, UserPostSchema, UserPutSchema, ErrorResponse
from typing import List
from ninja import Form, File, UploadedFile
from modules.utils.permission.permissions import AdminPermission


@api_controller(
    '/users',
    tags=['Rota - Usuários'],
)

class UsersController:
    
    services = Services
    
    @route.get('', response={200: List[UserListSchema]})
    def list(self, request):
        return self.services.list()
    
    @route.get('/{id}', response={200: UserListSchema})
    def get(self, request, id: int):
        return self.services.get(id=id)
    
    @route.post('', response={201: UserListSchema, 500: ErrorResponse}, auth=None)
    def post(self, request, payload: UserPostSchema = Form(...), profile_picture: UploadedFile = File(None)):
        
        return self.services.post(payload=payload.dict(), file=profile_picture)
    
    @route.put('/{id}', response={201: UserListSchema, 400: ErrorResponse, 500: ErrorResponse})
    def put(self, request, id: int, payload: UserPutSchema = Form(...)):
        return self.services.put(id=id, payload=payload.dict())
    
    @route.delete('/{id}', response={204: None})
    def delete(self, request, id: int):
        return self.services.delete(id=id)
    
    @route.put('picture/{id}', response={201: UserListSchema, 404: ErrorResponse, 500: ErrorResponse})
    def put_picture(self, request, id: int, profile_picture: UploadedFile = File(...)):
        return self.services.put_picture(id=id, file=profile_picture)
```

## Models

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    REQUIRED_FIELDS = ['password', 'username']
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return f'{self.username} - {self.email}'
    
    
```

## Repository

```python
import os
from typing import Dict, Optional
from core import settings
from ninja import UploadedFile, File
from modules.users.models import User
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password


class Repository:
    
    model = User
    
    @classmethod
    def list(cls) -> models.QuerySet:
        return cls.model.objects.all().order_by("id")
    
    @classmethod
    def get(cls, *, id: int) -> models.Model:
        return get_object_or_404(cls.model, id=id)


    @classmethod
    def password_hash(cls, password: str) -> str:
        password_hashed = make_password(password)
        return password_hashed

    @classmethod
    def update_payload(
        cls, *, payload: Dict, **kwargs
    ) -> Dict:
        
        if "password" in payload:
            payload["password"] = cls.password_hash(payload["password"])
        
        if "role" in payload and payload["role"] == "admin":
            payload["is_superuser"] = True
            payload["is_staff"] = True
        else:
            payload["is_superuser"] = False
            payload["is_staff"] = False
            
        
        updated_payload: Dict = {
            **payload
        }
        return updated_payload
    
    @classmethod
    def post(cls, *, payload: Dict, file: Optional[UploadedFile] = File(None), **kwargs) -> models.Model:
        
        if file:
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'profile_pictures')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            file_name = f"{file.name}"

            file_path = os.path.join(upload_dir, file_name)

            with open(file_path, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            payload["profile_picture"] = os.path.join('profile_pictures', file_name)
        
        
        payload = cls.update_payload(payload=payload)
        return cls.model.objects.create(**payload)
    
    @classmethod
    def put(
        cls,
        *,
        id: int,
        instance: models.Model,
        payload: Dict,
        **kwargs
    ) -> models.Model:
        
        instance = cls.get(id=id)
    
        for attr, value in payload.items():
            if value:
                setattr(instance, attr, value)
                print(f"{attr} = {value}")
        instance.save()
    
        return instance
    
    @classmethod
    def delete(
        cls, *, instance: models.Model
        ) -> models.Model:
        instance.delete()
        return instance
    
    
    @classmethod
    def put_picture(
        cls,
        *,
        id: int,
        file: UploadedFile,
        **kwargs
    ) -> models.Model:
        
        instance = cls.get(id=id)
        
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'profile_pictures')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_name = f"{file.name}"

        file_path = os.path.join(upload_dir, file_name)

        with open(file_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
        instance.profile_picture = os.path.join('profile_pictures', file_name)
        instance.save()
        return instance
```

## Schemas

```python
from enum import Enum
from typing import Optional
from ninja import Schema, UploadedFile, Field
from datetime import datetime


class RoleFilterEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserPostSchema(Schema):
    username: str
    email: str
    password: str
    role: RoleFilterEnum
    
class UserPutSchema(Schema):
    username: str = Field(None, alias="username", required=False, title="Nome de usuário")
    email: str = Field(None, alias="email", required=False, title="Email")
    password: str = Field(None, alias="password", required=False, title="Senha")
    role: RoleFilterEnum = None
    
class UserListSchema(Schema):
    id: int
    username: str
    email: str
    role: str
    profile_picture: Optional[str] = None
    date_joined: datetime
    last_login: datetime
    is_active: bool
    
    
class ErrorResponse(Schema):
    message: str
```

## Services

```python
from core import settings
from ninja import UploadedFile, File
import os
from typing import Any, Dict, Optional, Tuple, List, Union
from .repository import Repository
from django.db import models
from django.http import Http404
from ninja_extra import status
from django.db import transaction, IntegrityError

class Services:
    
    repository = Repository
    whitelist_disable_models: List[Optional[str]] = []
    
    @classmethod
    def validate_payload(
        cls, *, payload: Dict[str, Any], id: Optional[int] = None, **kwargs
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        instance: Optional[models.Model] = None
        return status.HTTP_200_OK, instance

    @classmethod
    def list(cls, *, filters: Optional[Any] = None) -> models.QuerySet:
        queryset = cls.repository.list()
        if filters:
            queryset = queryset.filter(**filters)
        return queryset
    
    @classmethod
    def get(cls, *, id: int) -> Tuple[int, models.Model | Dict[str, str]]:
        try:
            return status.HTTP_200_OK, cls.repository.get(id=id)
        except Http404:
            return status.HTTP_404_NOT_FOUND, {"message": (
                f"{cls.repository.model._meta.verbose_name.capitalize()} not found"
                ' não existe'
            ) }
        
    @classmethod
    def post(
        cls, *, payload: Dict[str, Any], file: Optional[UploadedFile] = File(None), **kwargs
    ) -> Tuple [int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message = cls.validate_payload(payload=payload)

                if status_code != status.HTTP_200_OK:
                    return status_code, message
                
                instance = cls.repository.post(payload=payload, file=file)
                return status.HTTP_201_CREATED, instance
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}

    @classmethod
    def put(
        cls,
        *,
        id: int,
        payload: Dict[str, Any],
        **kwargs
    ) -> Tuple[int, Union[models.Model, Dict[str, str]]]:
        
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message_or_object = cls.validate_payload(
                    payload=payload, id=id
                )

                if status_code != status.HTTP_200_OK:
                    message: Dict[str, str] = message_or_object
                    return status_code, message
                
                instance: models.Model = message_or_object

                instance = cls.repository.put(
                    instance=instance, payload=payload, id=id,
                )
                return status.HTTP_201_CREATED, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
        
    @classmethod
    def delete(
        cls, *, id: int, **kwargs
    ) -> Tuple[int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message_or_object: Dict[str, str] | models.Model

                status_code, message_or_object = cls.get(id=id)
                if status_code != status.HTTP_200_OK:
                    return status_code, message_or_object
                
                instance: models.Model = message_or_object

                instance = cls.repository.delete(instance=instance)

                return status.HTTP_204_NO_CONTENT, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
        
    @classmethod
    def put_picture(
        cls,
        *,
        id: int,
        file: UploadedFile,
        **kwargs
    ) -> Tuple[int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message_or_object: Dict[str, str] | models.Model

                status_code, message_or_object = cls.get(id=id)
                if status_code != status.HTTP_200_OK:
                    return status_code, message_or_object
                
                instance: models.Model = message_or_object

                instance = cls.repository.put_picture(
                    instance=instance, file=file, id=id
                )

                return status.HTTP_201_CREATED, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
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
# Generated by Django 5.1.4 on 2024-12-11 02:18

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=80, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

```

## 0002_alter_user_password

```python
# Generated by Django 5.1.4 on 2024-12-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]

```

## __init__

```python

```

