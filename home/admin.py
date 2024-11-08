from django.contrib import admin
from .models import *

myModels = [People, Colors, PeopleAddress]

# or 
# if not importing models as a seperate thing
# myModels = [models.People,models.Colors, models.PeopleAddress] # iterable list


# Register your models here.
# admin.site.register(People)
# admin.site.register(Colors)
# admin.sitte.register(PeopleAddress)

# alternative way to register multiple models
# register function accept a single model name or iterable,

admin.site.register(myModels)