from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Developer(models.Model):
    developer_id = models.AutoField(primary_key=True)
    developer_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    project_by = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name


class Tower(models.Model):
    tower_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    tower_name = models.CharField(max_length=500)
    no_of_floors = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.project_id.project_name) + "->" + str(self.tower_name)


class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    tower_id = models.ForeignKey(Tower, on_delete=models.CASCADE)
    floor_no = models.IntegerField(null=True, blank=True)
    no_of_flats = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.tower_id.tower_name) + " -> " + str(self.floor_no)


STATUS = (
    ('Unsold', 'Unsold'),
    ('Sold', 'Sold'),
    ('Booked', 'Booked'),
    ('Reserved', 'Reserved'),
)


class Flat(models.Model):
    flat_id = models.AutoField(primary_key=True)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)
    flat_no = models.IntegerField(null=True, blank=True)
    no_of_bedrooms = models.IntegerField(null=True, blank=True)
    floor_space = models.CharField(max_length=250, null=True, blank=True)
    no_of_balconies = models.IntegerField(null=True, blank=True)
    balconies_space = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.floor_id) + "->" + str(self.flat_no)


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cust_phone = models.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    cust_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cust_name
