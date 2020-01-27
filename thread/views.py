from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, TemplateView, ListView
from .models import Topic, Category
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

    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'thread/confirm_topic.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'thread/create_topic.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            # 正常動作ではここは通らない。エラーページへの遷移でも良い
            return redirect(reverse_lazy('base:top'))


class CategoryView(ListView):
    template_name = 'thread/category.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.filter(category__url_code=self.kwargs['url_code'])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = get_object_or_404(Category, url_code=self.kwargs['url_code'])
        return ctx


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
