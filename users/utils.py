from django.shortcuts import redirect

class AnonymousOnlyMixin:
    """
    Для запрета доступа аутентифицированным пользователям.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:main')
        return super().dispatch(request, *args, **kwargs)
