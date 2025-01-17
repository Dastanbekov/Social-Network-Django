class NavbarMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Наследуем существующий контекст
        context['menu'] = self.get_navbar_context()
        return context

    def get_navbar_context(self):
        # Генерируем меню в зависимости от аутентификации пользователя
        menu = [
            {'title': 'Home', 'url_name': 'main:main'},
            {'title': 'About', 'url_name': 'main:about'},
        ]

        if self.request.user.is_authenticated:
            menu += [
                {'title': 'Profile', 'url_name': 'users:profile'},
                {'title': 'Logout', 'url_name': 'users:logout'},
            ]
        else:
            menu += [
                {'title': 'Login', 'url_name': 'users:login'},
                {'title': 'Sign Up', 'url_name': 'users:register'},
            ]
        return menu