from django import forms

from .constants import STATES


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['city'].initial = self.request.GET['city'] if 'city' in self.request.GET else ''
        self.fields['state'].initial = self.request.GET['state'] if 'state' in self.request.GET else ''

    city = forms.CharField(label='City:', widget=forms.TextInput(attrs={'class': 'search-input', 'placeholder': 'City'}), required=False)
    state = forms.ChoiceField(label='State:', choices=STATES, widget=forms.Select(attrs={'class': 'search-input select-input'}), required=False)
