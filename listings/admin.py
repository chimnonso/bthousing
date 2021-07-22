from django.contrib import admin
from django.db import models
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'address', 'description', 'price', 'city' , 'state', 'zipcode')
    list_editable = ('is_published',)
    list_per_page = 25
    list_filter = ('realtor',)

admin.site.register(Listing, ListingAdmin)
