from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = "base/top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Django学習サイト"
        return context

