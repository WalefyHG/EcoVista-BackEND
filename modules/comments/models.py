from django.db import models

class CommentsModel(models.Model):
        
        comment = models.TextField()
        datetime_comment = models.DateTimeField(auto_now_add=True)
        status_comment = models.BooleanField(default=False)
        
        #Foreign Keys
        
        user = models.ForeignKey('users.User', on_delete=models.CASCADE)
        picture = models.ForeignKey('picture.PictureModel', on_delete=models.CASCADE)
        
        def __str__(self):
            return self.comment