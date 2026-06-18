from django.urls import path
from website.views import *

urlpatterns=[
    path('',index_view),
    path('aboute', aboute_view),
    path('contact', contact_view)

]