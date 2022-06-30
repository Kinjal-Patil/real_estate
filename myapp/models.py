from django.db import models


# Create your models here.
class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    project_by = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name


class Tower(models.Model):
    tower_id = models.IntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    tower_name = models.CharField(max_length=500)
    no_of_floors = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.tower_name


class Floor(models.Model):
    floor_id = models.IntegerField(primary_key=True)
    tower_id = models.ForeignKey(Tower, on_delete=models.CASCADE)
    no_of_flats = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.floor_id


STATUS = (
    ('Unsold', 'Unsold'),
    ('Sold', 'Sold'),
    ('Booked', 'Booked'),
    ('Reserved', 'Reserved'),
)


class Flat(models.Model):
    flat_id = models.IntegerField(primary_key=True)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)
    no_of_bedrooms = models.IntegerField(null=True, blank=True)
    floor_space = models.CharField(max_length=250, null=True, blank=True)
    no_of_balconies = models.IntegerField(null=True, blank=True)
    balconies_space = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.flat_id


class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cust_phone = models.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    cust_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cust_name
