from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from info_monitor.form import SaveUsedInfoForm
from info_monitor.models import Infos
from django.urls import reverse_lazy
from django.contrib import messages
from info_monitor.models import Infos
# Create your views here.
class AddUsedInfo(CreateView):
    template_name = "info_monitor/saveused.html"
    form_class = SaveUsedInfoForm
    #model = Infos
    success_url = reverse_lazy()





class ManageInfos(TemplateView):
    def get(self, request):
        # <view logic>
        print("get")
        return render(request, "info_monitor/saveused.html")

    def post(self, request):
        form = SaveUsedInfoForm(request.POST)

        if form.is_valid():
            print("it is valid")
            form.save()
            return HttpResponse("successfully saved")

        else:
            messages.error(request, "Error")
            return HttpResponse("Because of error could not save info")
        return render(request, "info_monitor/saveused.html", {"form": SaveUsedInfoForm()})





def search_if_name_is_used(request):
    is_query=False
    queryset=None
    zipcodes=request.POST.get("zipcode")
    mname = request.POST.get("middlename")
    firstname = request.POST.get("f_name")
    lastname = request.POST.get("l_name")
    age = request.POST.get("age")




    if zipcodes and firstname and lastname and mname and age  is not "":
        queryset = Infos.objects.filter(f_name__iexact=firstname.strip(), l_name__iexact=lastname.strip(), middlename__iexact=mname.strip(),
                                        zipcode=zipcodes.strip(),age=age.strip())
        if queryset:
            is_query = True

    elif zipcodes and firstname and lastname and mname  is not "":

        queryset = Infos.objects.filter(f_name__iexact=firstname.strip(), l_name__iexact=lastname.strip(),middlename__iexact=mname.strip(), zipcode=zipcodes.strip())
        if queryset:
            is_query=True
    elif zipcodes and firstname and lastname  is not "":

        queryset=Infos.objects.filter(f_name__iexact=firstname.strip(),l_name__iexact=lastname.strip(),zipcode=zipcodes.strip())
        if queryset:
            is_query=True

    return render(request,"info_monitor/saveused.html",context={"present":is_query,"records":queryset})





def purify_text(text):
    return text.lower().strip()