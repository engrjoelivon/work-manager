from django.conf.urls import url

from info_monitor.views import ManageInfos,search_if_name_is_used


urlpatterns =[
     url(r'^$',ManageInfos.as_view(),name="home"),
   url(r'^search$',search_if_name_is_used,name="search_if_name_is_use"),



]