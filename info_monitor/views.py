from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from info_monitor.form import SaveUsedInfoForm
from info_monitor.models import Infos
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.forms.models  import model_to_dict
from info_monitor.models import Infos

import json
# Create your views here.
class AddUsedInfo(CreateView):
    template_name = "info_monitor/saveused.html"
    form_class = SaveUsedInfoForm
    #model = Infos
    success_url = reverse_lazy()





class ManageInfos(TemplateView):
    def get(self, request):
        # <view logic>
        #print("get")
        #Get_all_records()
        return render(request, "info_monitor/saveused.html",{"form": SaveUsedInfoForm()})

    def post(self, request):
        form = SaveUsedInfoForm(request.POST,request.FILES)

        if form.is_valid():
            print("it is valid")
            form.save()
            return HttpResponseRedirect(reverse('success'))
        else:
            print(form.errors)

            #messages.error(request, "Error")
            #return HttpResponse("Because of error could not save info")
        return render(request, "info_monitor/saveused.html", {"form": form})





def search_if_name_is_used(request):
    is_query=False
    queryset=None
    zipcodes=request.POST.get("zipcode")
    mname = request.POST.get("middlename")
    firstname = request.POST.get("f_name")
    lastname = request.POST.get("l_name")
    age = request.POST.get("age")

    try:


        if zipcodes and firstname and lastname and mname and age  is not "":
            queryset = Infos.objects.filter(f_name__iexact=firstname.strip(), l_name__iexact=lastname.strip(), middlename__iexact=mname.strip(),
                                        zipcode=zipcodes.strip(),age=age.strip())
            if queryset:
                is_query = True

        elif zipcodes and firstname and lastname and mname  is not "":

            queryset = Infos.objects.filter(f_name__iexact=firstname.strip(), l_name__iexact=lastname.strip(),middlename__iexact=mname.strip(), zipcode=zipcodes.strip())
            if queryset:
                is_query=True

        elif firstname and lastname and age  is not "":

            queryset=Infos.objects.filter(f_name__iexact=firstname.strip(),l_name__iexact=lastname.strip(),age=age.strip())
            if queryset:
                is_query=True


        elif firstname and lastname and mname is not "":

            queryset = Infos.objects.filter(f_name__iexact=firstname.strip(), l_name__iexact=lastname.strip(),middlename__iexact=mname.strip())
            if queryset:
                is_query = True

        elif firstname and lastname  is not "":

            queryset = Infos.objects.filter(f_name__iexact=firstname.strip(), l_name__iexact=lastname.strip())
            if queryset:
                is_query = True
        elif zipcodes is not "":
           queryset=Infos.objects.filter(zipcode=zipcodes.strip())
           if queryset:
                is_query=True

        else:
            queryset = Infos.objects.all()
            if queryset:
                is_query=True


    except AttributeError:
        pass
    except:
        pass
    return render(request,"info_monitor/saveused.html",context={"present":is_query,"records":queryset,"form": SaveUsedInfoForm()})





def purify_text(text):
    return text.lower().strip()






class Get_all_records():


    def __init__(self):
     rec_query=   Infos.objects.all()
     self.list_of_rec=[]
     for rec in rec_query:
             self.list_of_rec.append(model_to_dict(rec,["zipcode","f_name","l_name","middlename","age","address","links"]))
     self.convert_to_json(self.list_of_rec)

    def convert_to_json(self,arg):
         json.dumps(arg)


    def  send_files_to_remote(self):
        pass
