from django.contrib import admin
from django.contrib.contenttypes import generic

from contacts.models import (PhoneNumber, EmailAddress,
                             WebSite, StreetAddress, SpecialDate, Location)
# Company


class EmailAddressInline(generic.GenericTabularInline):
    model = EmailAddress


class PhoneNumberInline(generic.GenericTabularInline):
    model = PhoneNumber


class WebSiteInline(generic.GenericTabularInline):
    model = WebSite


class StreetAddressInline(generic.GenericStackedInline):
    model = StreetAddress


class SpecialDateInline(generic.GenericStackedInline):
    model = SpecialDate


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline,
        EmailAddressInline,
        WebSiteInline,
        StreetAddressInline,
        SpecialDateInline,
    ]

    list_display = ('name',)
    search_fields = ['^name', ]
    prepopulated_fields = {'slug': ('name',)}


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline,
        EmailAddressInline,
        WebSiteInline,
        StreetAddressInline,
        SpecialDateInline,
    ]

    list_display_links = ('first_name', 'last_name',)
    list_display = ('first_name', 'last_name', 'company',)
    list_filter = ('company',)
    ordering = ('last_name', 'first_name')
    search_fields = ['^first_name', '^last_name', '^company__name']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


class GroupAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'date_modified')
    ordering = ('-date_modified', 'name',)
    search_fields = ['^name', '^about', ]
    prepopulated_fields = {'slug': ('name',)}


class LocationAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'date_modified')
    ordering = ('weight', 'name')
    search_fields = ['^name', ]
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (None, {
            'fields': (('name', 'slug',),)
        }),
        ('Advanced options', {
            'fields': (('is_phone', 'is_street_address'),)
        })
    )

#admin.site.register(Company, CompanyAdmin)
#admin.site.register(Person, PersonAdmin)
admin.site.register(Location, LocationAdmin)
