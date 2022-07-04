from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Project)
admin.site.register(Tower)
admin.site.register(Floor)
admin.site.register(Flat)
admin.site.register(Customer)
admin.site.register(Developer)
