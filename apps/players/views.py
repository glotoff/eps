from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('players/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        print("load_template=" + load_template)

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('players/' + load_template)

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class PlayerListView(ListView):
    model = Player
    template_name = 'player_list.html'


class PlayerCreateView(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'date_of_birth', 'batting_style', 'bowling_style', 'role', 'club']
    template_name = 'player_form.html'

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('first_name')
    serializer_class = PlayerSerializer