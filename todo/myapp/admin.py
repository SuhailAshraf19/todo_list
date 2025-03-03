from django.contrib import admin
from .models import profile, List, Items

# Register your models here.
@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    list_display=('user', 'photo','address','description','phone_number')
    search_fields=('phone_number','user')
admin.site.register(List)  # Register the List model
admin.site.register(Items)  # Register the Item model    