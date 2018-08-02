import requests
import json
import socket

from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import SearchForm


class SearchView(FormView):
    form_class = SearchForm
    success_url = reverse_lazy('trail_search:results')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if 'search' in self.request.GET:
            city = self.request.GET['city'] if 'city' in self.request.GET else ''
            state = self.request.GET['state'] if 'state' in self.request.GET else ''
            if self.request.GET['search'] == 'search':
                endpoint = f'https://trailapi-trailapi.p.mashape.com/?q[activities_activity_type_name_eq]=mountain+biking&q[city_cont]={city}&q[state_cont]={state}'
            else:
                lat = self.request.GET['lat'] if 'lat' in self.request.GET else ''
                lon = self.request.GET['lon'] if 'lon' in self.request.GET else ''
                endpoint = f'https://trailapi-trailapi.p.mashape.com/?q[activities_activity_type_name_eq]=mountain+biking&lat={lat}&lon={lon}&radius=25'
            s = requests.Session()
            s.headers.update({'Accept': 'text/plain', 'X-Mashape-Key': '54lXQ1oTXHmshd3CW3lqEEaJaIt4p1lmHYDjsncC76WrSHS0mp'})
            r = s.get(endpoint)
            places = r.content.decode('utf8')
            data = json.loads(places)['places']
            context['city'] = city
            context['state'] = state
            context['places'] = data
        return context

    def get_form_kwargs(self):
        kw = super(SearchView, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    def form_valid(self, form):
        if 'around_me' in self.request.POST:
            print('around_me')
        else:
            print('search')
        return super().form_valid(form)


class TrailSearch(SearchView):
    template_name = 'trail_search/search.html'
