from django.contrib import admin

from .models import *


admin.site.register(Service)
admin.site.register(Worker)
admin.site.register(Client)
admin.site.register(Case)
admin.site.register(Request)
