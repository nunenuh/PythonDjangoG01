from django import forms
from orm.models import Province


class ProvinceForm(forms.Form):
    id = forms.CharField(required=False)    
    name = forms.CharField(required=True)
    
    class Meta:
        model = Province

