from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



# Error Pages

def handle_404(request, exceptions):
    template_name = 'errors/handle_404.html'
    return render(request, template_name)


def handle_500(request, exceptions):
    template_name = 'errors/handle_404.html'
    return render(request, template_name)


class Index(TemplateView):
    template_name = 'core/index.html'