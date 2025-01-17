from django.shortcuts import redirect

class RedirectAuthUserMixin:
    def dispatch(self, request, *args, **kwargs):
        redirect_url = 'users:login'
        if request.user.is_authenticated:
            return redirect(redirect_url)
        return super().dispatch(request, *args, **kwargs)
