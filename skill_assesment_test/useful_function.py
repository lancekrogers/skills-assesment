# A File for usefull Function
from django.contrib import admin


def register(list_of_mods):
    """
        Provide a list of models to register and run the function
    """
    for i in list_of_mods:
        admin.site.register(i)
