from django.db import models


class ReportModel(models.Model):

    type_report = models.CharField(max_length=255)
    message = models.TextField()
    date_report = models.DateTimeField(auto_now_add=True)
    status_report = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    
    #Foreign Keys
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.ForeignKey('comments.CommentsModel', on_delete=models.CASCADE)
    picture = models.ForeignKey('picture.PictureModel', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type_report
    