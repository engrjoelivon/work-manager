from django import forms
from info_monitor.models import Infos


class SaveUsedInfoForm(forms.ModelForm):
    def save(self, commit=True):


        if commit is True:
            user = super().save(commit=False)  # return the User table object,save the table but dont commit the data            user.set_password(user.password) #call the setpassword method of the user table            user.email=user.username       #add the email to the to be the username            if fname is not None:





        #if user.address is None:
        print("address is ",user.address)
            #user.address = " "
        #if user.links is None:
            #user.links=" "


        user.save()  # now save the userobject            return user



    class Meta:
        model = Infos
        fields = ["zipcode","f_name","l_name","middlename","age","address","links"]
