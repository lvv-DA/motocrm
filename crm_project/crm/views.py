from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SalesRepresentative, Customer, Contact, Location, Opportunity, Client
from .serializers import (
    SalesRepresentativeSerializer, CustomerSerializer, ContactSerializer,
    LocationSerializer, OpportunitySerializer, ClientSerializer
)

# API Root View
class ApiRootView(APIView):
    """
    Root view for the API. Lists all the available endpoints.
    """
    def get(self, request):
        return Response({
            "message": "Welcome to the CRM API",
            "available_endpoints": {
                "Sales Representatives": "/api/salesrepresentatives/",
                "Customers": "/api/customers/",
                "Contacts": "/api/contacts/",
                "Locations": "/api/locations/",
                "Opportunities": "/api/opportunities/",
                "Clients": "/api/clients/",
            }
        })


# Sales Representative Views
class SalesRepresentativeList(generics.ListCreateAPIView):
    """
    Handles listing and creating Sales Representatives.
    """
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer


class SalesRepresentativeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single Sales Representative.
    """
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer


# Customer Views
class CustomerList(generics.ListCreateAPIView):
    """
    Handles listing and creating Customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single Customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Contact Views
class ContactList(generics.ListCreateAPIView):
    """
    Handles listing and creating Contacts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single Contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Location Views
class LocationList(generics.ListCreateAPIView):
    """
    Handles listing and creating Locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single Location.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# Opportunity Views
class OpportunityList(generics.ListCreateAPIView):
    """
    Handles listing and creating Opportunities.
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


class OpportunityDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single Opportunity.
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


# Client Views
class ClientList(generics.ListCreateAPIView):
    """
    Handles listing and creating Clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single Client.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
