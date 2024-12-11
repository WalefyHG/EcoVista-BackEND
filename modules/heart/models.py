from django.db import models

class HeartModel(models.Model):
    
    date = models.DateTimeField(auto_now_add=True)
    
    #Foreign Keys
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    picture = models.ForeignKey('picture.PictureModel', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username + ' - ' + self.picture.title