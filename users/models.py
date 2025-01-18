from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Follow(models.Model):
    # Пользователь, который подписался
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    
    # Пользователь, на которого подписались
    followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f'{self.user} follows {self.followed_user}'
