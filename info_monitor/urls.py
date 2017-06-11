from django.conf.urls import url
from info_monitor import views
from django.views.generic import TemplateView
from info_monitor.models import Infos
from info_monitor.views import ManageInfos


urlpatterns =[
     url(r'^$',ManageInfos.as_view(),name="home"),
   # url(r'^$',TemplateView.as_view(model="Usedinfo",template_name= "info_monitor/check.html")),



]