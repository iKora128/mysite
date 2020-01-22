from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView
from .models import Topic
from .forms import TopicCreateForm


class TopicDetailView(DetailView):
    template_name = 'thread/detail_topic.html'
    model = Topic
    context_object_name = 'topic'


class TopicCreateView(CreateView):
    template_name = 'thread/create_topic.html'
    form_class = TopicCreateForm
    model = Topic
    success_url = reverse_lazy('base:top')


'''
def topic_create(request):
    template_name = "thread/create_topic.html"
    ctx = {}
    if request.method == "GET":
        ctx["form"] = TopicCreateForm()
        return render(request, template_name, ctx)

    if request.method == "POST":
        topic_form = TopicCreateForm(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            return redirect(reverse_lazy("base:top"))
        else:
            ctx["form"] = topic_form
            return render(request, template_name, ctx)
'''
