from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

# USER_STATUS_OPTIONS = (
#     ('N', 'Newbie'), 
#     ('P', 'Pro')
# )

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now())
    solved = models.BooleanField(default=False)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self) -> str:
        return self.content
