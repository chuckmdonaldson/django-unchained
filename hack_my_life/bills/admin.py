from django.contrib import admin
from bills.models import Category,Creditor,PaymentMethod,PaymentProvider,Schedule
# Register your models here.
admin.site.register(Category)
admin.site.register(Creditor)
admin.site.register(PaymentMethod)
admin.site.register(PaymentProvider)
admin.site.register(Schedule)
