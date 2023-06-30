from django import forms 
from . import models

class CelebrityModelForm(forms.ModelForm):
    def clean_net_worth(self):
        input_ = self.cleaned_data['net_worth']
        if input_ < 100000:
            raise forms.ValidationError('Net Worth must be > than 10000')
        return input_

    class Meta:
        model = models.Celebrity
        fields = '__all__'