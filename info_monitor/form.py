from django import forms
from django.forms import SelectDateWidget

from info_monitor.models import Infos


class SaveUsedInfoForm(forms.ModelForm):
    BIRTH_YEAR_CHOICES = ['1949','1950', '1951', '1952','1953','1954','1955']
    zipcode=forms.IntegerField(label="Zipcode",max_value=99999,widget=forms.NumberInput,help_text="must be filled")
    f_name = forms.CharField(label="Firstname",widget=forms.TextInput)
    l_name=forms.CharField(label="Lastname")
    middlename= forms.CharField(label="Middlename",required=False)
    address = forms.CharField(label="Address",required=False)
    age =forms.IntegerField(label="Age",required=False,max_value=100,initial=0)
    links=forms.URLField(max_length=1000,required=False,widget=forms.URLInput)
    myfile=forms.FileField(required=False,widget=forms.FileInput)
    where = forms.ChoiceField(widget=forms.Select,choices=Infos().sites_info_obtained,required=False)
    dob = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES),required=False)
    status =forms.BooleanField(widget=forms.CheckboxInput,required=False)

    def save(self, commit=True):


        if commit is True:
            user = super().save(commit=False,)  # return the User table object,save the table but dont commit the data            user.set_password(user.password) #call the setpassword method of the user table            user.email=user.username       #add the email to the to be the username            if fname is not None:
            #if user.address is None:
            user.f_name=self.names_to_lower(user.f_name)
            user.l_name=self.names_to_lower(user.l_name)
            user.middlename=self.names_to_lower(user.middlename)
            user.save()  # now save the userobject            return user





    def names_to_lower(self,arg):
        return self.purify_text(arg)



    def purify_text(self,text):
        return text.lower().strip()

    class Meta:
        model = Infos

        fields = ["status","zipcode","f_name","l_name","middlename","age","address","links","myfile","where","dob"]




