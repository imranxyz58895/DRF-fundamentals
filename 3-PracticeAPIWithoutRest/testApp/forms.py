from django import forms 
from . import models

class CelebrityModelForm(forms.ModelForm):
    class Meta:
        model = models.Celebrity
        fields = '__all__'