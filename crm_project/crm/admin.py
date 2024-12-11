from django.contrib import admin
from .models import User, SalesRepresentative, Customer, Contact, Location, Opportunity, Client

admin.site.register(User)
admin.site.register(SalesRepresentative)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Location)
admin.site.register(Opportunity)
admin.site.register(Client)