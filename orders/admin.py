from django.contrib import admin
from .models import Order, Rider


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_phone', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('customer_name', 'customer_phone')


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'phone')
