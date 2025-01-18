from django.shortcuts import redirect
from .models import Follow
class AnonymousOnlyMixin:
    """
    Для запрета доступа аутентифицированным пользователям.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:main')
        return super().dispatch(request, *args, **kwargs)

class FollowMixin:
    def get_followers_count(self, user):
        return Follow.objects.filter(followed_user=user).count()

    def get_following_count(self, user):
        return Follow.objects.filter(user=user).count()

    def is_following(self, user, followed_user):
        return Follow.objects.filter(user=user, followed_user=followed_user).exists()
