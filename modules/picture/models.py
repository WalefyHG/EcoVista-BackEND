from django.db import models

class PictureModel(models.Model):
    
    image = models.ImageField(upload_to='images/')
    date_capture = models.DateField(blank=True, null=True)
    localization_picture = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    # Foreign Keys
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    biome = models.ForeignKey('biomes.BiomeModel', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.image.url