from django.contrib import admin
from clubmates.lib.apps.clubmates.models import Location, Message, User
    
admin.site.register(Location)
admin.site.register(Message)
admin.site.register(User)