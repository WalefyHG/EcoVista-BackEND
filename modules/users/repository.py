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
        file: Optional[UploadedFile] = File(None),
        **kwargs
    ) -> models.Model:
        
       instance = cls.get(id=id)

    # Atualizar o payload (a lógica de atualização de senha ou outros campos pode ser aqui)
       payload = cls.update_payload(payload=payload)

    # Se um arquivo for enviado, salva o arquivo e adiciona o caminho ao payload
       if file:
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'profile_pictures')

        # Criar o diretório se não existir
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

        # Define o nome do arquivo
            file_name = f"{instance.id}_{file.name}"
            file_path = os.path.join(upload_dir, file_name)

        # Salva o arquivo
            with open(file_path, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        # Atualiza o campo profile_picture no payload
            payload["profile_picture"] = os.path.join('profile_pictures', file_name)

    # Atualiza os atributos da instância apenas se o valor não for None
       for attr, value in payload.items():
            if value is not None:  # Verifica se o valor não é None antes de atribuir
                setattr(instance, attr, value)
                print(f"{attr} = {value}")  # Print para debugar

       instance.save()
    
       return instance
    
    @classmethod
    def delete(
        cls, *, instance: models.Model
        ) -> models.Model:
        instance.delete()
        return instance
    