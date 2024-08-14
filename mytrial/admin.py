from django.contrib import admin
from .models import Profile,CaseFile,PassTicket,Payment

admin.site.register(PassTicket)
admin.site.register(Payment)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'gender', 'county', 'is_admin', 'created_at', 'updated_at')
    search_fields = ('user__username', 'first_name', 'last_name', 'phone_number', 'county')
    list_filter = ('gender', 'county', 'is_admin')


class CaseFileAdmin(admin.ModelAdmin):
    list_display = (
        'tenant', 
        'postal_address', 
        'telephone_number', 
        'landlord_name', 
        'agent', 
        'caretaker', 
        'auctioneer', 
        'duration_of_stay', 
        'monthly_rent', 
        'year_of_entry', 
        'deposit_paid', 
        'cause_of_action', 
        'problem', 
        'ocs_police_station', 
        'status', 
        'created_at'
    )
    search_fields = (
        'tenant', 
        'landlord_name', 
        'agent', 
        'caretaker', 
        'auctioneer', 
        'cause_of_action', 
        'ocs_police_station'
    )
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

admin.site.register(CaseFile, CaseFileAdmin)
