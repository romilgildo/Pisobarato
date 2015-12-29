
from django.contrib import admin

# Register your models here.

from pisobarato.models import Piso, Imagen

admin.site.register(Piso)
admin.site.register(Imagen)