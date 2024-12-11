from django.db import models


class BiomeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ForeignKey('picture.PictureModel', on_delete=models.CASCADE, blank=True, null=True)
    vegetetion_predominance = models.CharField(max_length=100, blank=True)
    fauna_predominance = models.CharField(max_length=100, blank=True)
    area = models.FloatField(blank=True, null=True)
    state_vegetetion = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    