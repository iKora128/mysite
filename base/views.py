from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from thread.models import Topic


def top(request):
    context = {"title": "Django学習サイト"}
    return render(request, "base/top.html", context)


class TopView(TemplateView):
    template_name = "base/top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Django学習サイト"
        return context


class TopicListView(ListView):
    template_name = "base/top.html"
    queryset = Topic.objects.order_by("-created")
    context_object_name = "topic_list"


