from django import forms
from info_monitor.models import Infos


class SaveUsedInfoForm(forms.ModelForm):
    class Meta:
        model = Infos
        fields = ["zipcode","middlename"]