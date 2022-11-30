from django.forms import ModelForm
from app.models import Cars

# Create the form class.
class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['model', 'brand', 'year']