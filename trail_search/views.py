from django.views.generic import TemplateView


class TrailSearch(TemplateView):
    template_name = 'trail_search/search.html'
