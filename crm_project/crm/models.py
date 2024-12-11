from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

# Sales Representative Model
class SalesRepresentative(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sales_representative")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Customer Model
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=40)
    contact_info = models.JSONField()  # Stores contact details as JSON
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name="customers")

    def __str__(self):
        return self.business_name

# Contact Model
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="contacts")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Location Model
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    manager = models.CharField(max_length=60)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="locations")

    def __str__(self):
        return f"Location {self.id} - {self.customer.business_name}"

# Opportunity Model
class Opportunity(models.Model):
    class Stage(models.TextChoices):
        RESEARCHING = "Researching"
        PROSPECTING = "Prospecting"
        QUALIFYING = "Qualifying"
        PITCHING = "Pitching"
        NEGOTIATING = "Negotiating"
        CLOSING = "Closing"

    id = models.AutoField(primary_key=True)
    description = models.TextField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    stage = models.CharField(
        max_length=20,
        choices=Stage.choices,
        default=Stage.RESEARCHING,
    )
    expected_close_date = models.DateField()
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name="opportunities")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="opportunities")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="opportunities")

    def __str__(self):
        return f"Opportunity {self.id} - {self.description[:50]}"

# Client Model
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="clients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
