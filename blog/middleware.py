from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        exempt_urls = [
            reverse('users:login'),
            reverse('users:register'),
        ]
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('users:login')  
        return self.get_response(request)