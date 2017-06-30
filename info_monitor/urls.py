from django.conf.urls import url
from django.views.generic import TemplateView
from info_monitor.views import ManageInfos,search_if_name_is_used,Get_all_records


urlpatterns =[
     url(r'^$',ManageInfos.as_view(),name="home"),
     url(r'^search$',search_if_name_is_used,name="search_if_name_is_use"),
     url(r'^success$',TemplateView.as_view(template_name="info_monitor/success.html"),name="success"),
url(r'^all',Get_all_records.as_view(),name="all"),
             ]