from django.db import models

# Create your models here.


from django.db import models


class File(models.Model):
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)