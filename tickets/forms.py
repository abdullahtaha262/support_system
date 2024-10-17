from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'picture']
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'picture': _('Picture'),
        }

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status']
        labels = {
            'status': _('Status'),
        }