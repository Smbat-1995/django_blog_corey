from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length = 100)
    content  = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User , on_delete = models.CASCADE) # if user is deleted then delete posts

    def __str__(self) -> str:
        return self.post_title