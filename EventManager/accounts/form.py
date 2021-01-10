from django import forms
from django.forms import ModelForm
from .models import Event_Registration

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

class EventRegistrationForm(forms.ModelForm):
	class Meta:
		widgets = {'event_name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
		 'description': forms.Textarea(attrs={'placeholder': 'Description Here', 'class': 'description_input_E_R '}),
		 'location': forms.TextInput(attrs={'placeholder': 'Location'}),
		 'starting_date': DateTimeInput(attrs={'class': 'date-time_input_E_R ', 'id': 'description_input_from_E_R '}), 
		 'ending_date': DateTimeInput(attrs={'class': 'date-time_input_E_R ', 'id': 'description_input_to_E_R '}), 
		 'registration_deadline': DateTimeInput(attrs={'class': 'date-time_input_E_R ', 'id': 'description_input_regdeadline_E_R '}), 
		 'host_email': forms.TextInput(attrs={'placeholder': 'Host Email'}),
		 'host_password': forms.PasswordInput(attrs={'placeholder': 'Host Password'})}
		model = Event_Registration
		fields = '__all__'