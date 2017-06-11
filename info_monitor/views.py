from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from info_monitor.form import SaveUsedInfoForm
from info_monitor.models import Infos
from django.urls import reverse_lazy
from django.contrib import messages
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
            return HttpResponse("done")

        else:
            messages.error(request, "Error")
            print("it is invalid")
        return render(request, "info_monitor/saveused.html", {"form": SaveUsedInfoForm()})





