from django import forms
from .validators import validate_dot_com, validate_url


class SubmitURLForm(forms.Form):
    url = forms.CharField(
            label='Submit URL', 
            validators=[validate_url,],
            widget = forms.TextInput(
                attrs = {'placeholder': 'Your URL' ,
                         'class': 'form-control'}
                )
            )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     url = cleaned_data.get('url')
    #     print(url) 


    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     if 'http' in url:
    #         return url
    
    #     return 'https://' + url