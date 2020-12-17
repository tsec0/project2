from django.views import generic as views


class WelcomePage(views.TemplateView):
    template_name = 'main/welcome.html'
