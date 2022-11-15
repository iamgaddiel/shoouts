from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



# Error Pages

def handle_404(request, exceptions):
    template_name = 'errors/error_404.html'
    return render(request, template_name)


def handle_500(request, exceptions):
    template_name = 'errors/handle_500.html'
    return render(request, template_name)


class Index(TemplateView):
    template_name = 'core/index.html'


class UserDashboard(TemplateView, LoginRequiredMixin):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


