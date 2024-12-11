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
    