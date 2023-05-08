from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='home'),
    path('hiv', views.hiv, name='hiv'),
    path('hivtestresults',views.result),
    path('malaria',views.malaria, name='malaria'),
    path('malariatestresults',views.malariaresult),
    path('TB',views.TB, name='TB'),
    path('tbtestresults',views.tbresult),
]


    