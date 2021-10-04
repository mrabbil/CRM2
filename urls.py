from django.contrib import admin
from django.urls import path, re_path
from djreservation import urls as accounts_urls
from demoapp.views import home, CRM2



urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    re_path(r"^reservation/create/(?P<modelpk>\d+)$",
            CRM2.as_view(), name="myreservation")
] + accounts_urls.urlpatterns
  