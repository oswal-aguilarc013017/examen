from django.contrib import admin
from .models import Plato, Menu, Union, PlatoAdmin, MenuAdmin

admin.site.register(Plato,PlatoAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Union)
