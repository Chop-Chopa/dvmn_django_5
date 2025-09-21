from django.contrib import admin

from .models import Flat, Complaint, Owner

class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['complainer', 'flat']

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = ('full_name', 'phonenumber', 'pure_phone')
    filter_horizontal = ('flats',)

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
