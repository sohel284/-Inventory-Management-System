from django.contrib import admin
from .models import Laptop, Mobile, Desktop

admin.site.register(Laptop)
admin.site.register(Desktop)
admin.site.register(Mobile)

