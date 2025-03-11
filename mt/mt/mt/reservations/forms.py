from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
        
class ReservationStatusForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['status']