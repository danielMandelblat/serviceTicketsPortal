from django.urls import include, path
from portal.views import tickets, test, new_ticket

urlpatterns = [
    path('tickets/', tickets, name='tickets'),
    path('test/', test, name='test'),
    path('new_ticket/', new_ticket, name='new_ticket'),
]