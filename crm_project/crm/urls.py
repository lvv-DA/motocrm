from django.urls import path
from .views import (
    ApiRootView,
    SalesRepresentativeList, SalesRepresentativeDetail,
    CustomerList, CustomerDetail,
    ContactList, ContactDetail,
    LocationList, LocationDetail,
    OpportunityList, OpportunityDetail,
    ClientList, ClientDetail,
)

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('salesrepresentatives/', SalesRepresentativeList.as_view(), name='salesrep-list-create'),
    path('salesrepresentatives/<int:pk>/', SalesRepresentativeDetail.as_view(), name='salesrep-detail'),
    path('customers/', CustomerList.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('contacts/', ContactList.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('locations/', LocationList.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('opportunities/', OpportunityList.as_view(), name='opportunity-list-create'),
    path('opportunities/<int:pk>/', OpportunityDetail.as_view(), name='opportunity-detail'),
    path('clients/', ClientList.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
]
