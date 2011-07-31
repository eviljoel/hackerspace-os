from django.forms import ModelForm
import django.forms as forms

from hos.cal.fields import DateTimeCombiField
from hos.cal.models import Event


class EventForm(ModelForm):
    """
    Form to add an event
    """

    startDate = DateTimeCombiField()
    endDate = DateTimeCombiField(required=False)
    teaser = forms.CharField(required=False)

    class Meta:
        model = Event
        exclude = ('where', 'created_at', 'created_by', 'deleted', 'who')
