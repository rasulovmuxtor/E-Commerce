from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('item',)
    fields = ('item','item_price','price','quantity')
    readonly_fields = ['item_price']
    extra=0
    def item_price(self, instance):
        try:
            if instance.quantity>1:
                return instance.price/instance.quantity
            return '    ->'
        except TypeError:
            return ''


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            if field.name=='status':
                value = getattr(obj,'get_status_display')()
            else:
                value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')

            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description='Export to Csv'






@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name','status','phone_number','order_detail','created')
    inlines = (OrderItemInline,)
    date_hierarchy = 'created'
    list_filter = ('status','created')
    actions = [export_to_csv]
    def order_detail(self,obj):
        url = reverse('admin_order_detail',args=[obj.id])
        return mark_safe(f'<a href="{url}">View</a>')