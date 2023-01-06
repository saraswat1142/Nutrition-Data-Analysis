from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include

from .views import (AAP_api, CAROTENOIDS_api, EOF_api, FAP_api, FSV_api,
                    MTE_api, OA_api, OPPS_api, PP_api, PPDF_api, SIS_api,
                    WSV_api,ALL)

urlpatterns = [
    path('PPDF/',PPDF_api),
    path('WSV/',WSV_api),
    path('FSV/',FSV_api),
    path('CAROTENOIDS/',CAROTENOIDS_api),
    path('MTE/',MTE_api),
    path('SIS/',SIS_api),
    path('FAP/',FAP_api),
    path('AAP/',AAP_api,name="aap_api"),
    path('OA/',OA_api),
    path('PP/',PP_api),
    path('OPPS/',OPPS_api),
    path('EOF/',EOF_api),
    path('ALL/',ALL),

]