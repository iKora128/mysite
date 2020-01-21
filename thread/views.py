from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, DetailView

from . models import Topic


class TopicDetailView(DetailView):
    template_name = 'thread/detail_topic.html'
    model = Topic
    context_object_name = 'topic'