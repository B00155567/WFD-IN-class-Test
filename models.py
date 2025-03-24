from django.db import models

# Car info - stores details about each car in the dealership
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)  # Unique ID for each car
    serial_number = models.CharField(max_length=100)  # Car's serial number
    make = models.CharField(max_length=100)  # Brand (Toyota, Honda, etc)
    model = models.CharField(max_length=100)  # Model name
    colour = models.CharField(max_length=50)  # Car color
    year = models.IntegerField()  # Manufacturing year
    car_for_sale_yn = models.BooleanField()  # Is it for sale?

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Customer info - stores customer details
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Unique ID for each customer
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Salesperson info - stores staff who sell cars
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)  # Unique ID for each salesperson
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Sales records - tracks when cars are sold
class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)  # Unique ID for each sale
    invoice_number = models.CharField(max_length=100)
    date = models.DateField()  # When the sale happened
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Which car was sold
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Who bought it
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)  # Who sold it

    def __str__(self):
        return f"Invoice {self.invoice_number}"

# Mechanic info - stores staff who fix cars
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)  # Unique ID for each mechanic
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Service types - different services offered
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)  # Unique ID for each service type
    service_name = models.CharField(max_length=200)  # Name of service
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Cost per hour

    def __str__(self):
        return self.service_name

# Service records - tracks car repairs
class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)  # Unique ID for each service
    service_ticket_number = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Car being serviced
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Car owner
    date_received = models.DateField()  # When car came in
    comments = models.TextField()  # Notes about the service
    date_returned_to_customer = models.DateField(null=True, blank=True)  # When car was returned

    def __str__(self):
        return f"Ticket {self.service_ticket_number}"

# Links mechanics to service jobs
class ServiceMechanic(models.Model):
    servicemechanic_id = models.AutoField(primary_key=True)  # Unique ID for each assignment
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  # Which service job
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Type of service
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)  # Who did the work
    hours = models.DecimalField(max_digits=5, decimal_places=2)  # How long it took
    comment = models.TextField()  # Notes about the work
    rate = models.DecimalField(max_digits=10, decimal_places=2)  # Hourly rate charged

    def __str__(self):
        return f"{self.mechanic} - {self.service}"

# Parts inventory
class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)  # Unique ID for each part type
    part_number = models.CharField(max_length=100)  # Part number/code
    description = models.TextField()  # What the part is
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # What we paid
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)  # What we charge

    def __str__(self):
        return self.part_number

# Tracks parts used in repairs
class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)  # Unique ID for each parts usage
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)  # Which part
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  # Which service
    number_used = models.IntegerField()  # How many used
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price charged

    def __str__(self):
        return f"{self.part} - {self.number_used} units"