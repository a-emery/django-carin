from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import UserForm


class UserAddView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'authentication/user_form.html'
    success_url = reverse_lazy('trail_search:search')

    def get_form_kwargs(self):
        kwargs = super(UserAddView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        if User.objects.filter(username=form.cleaned_data['email']).exists():
            form.add_error('email', 'There is already a user with that e-mail')
            return self.form_invalid(form)
        return super(UserAddView, self).form_valid(form)