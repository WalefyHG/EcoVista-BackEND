# Repository

from .models import BiomeModel
from django.db import models
from django.shortcuts import get_object_or_404

class Repository:
    
    model = BiomeModel
    
    @classmethod
    def get_all(cls):
        return cls.model.objects.all()
    
    @classmethod
    def get_by_id(cls, id):
        return get_object_or_404(cls.model, id=id)
    
    @classmethod
    def get_by_name(cls, name):
        return get_object_or_404(cls.model, name=name)
    
    @classmethod
    def post(cls, data):
        return cls.model.objects.create(**data)
    
    @classmethod
    def put(cls, id, data):
        instance = cls.get_by_id(id)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    @classmethod
    def delete(cls, id):
        instance = cls.get_by_id(id)
        instance.delete()
        return instance
    