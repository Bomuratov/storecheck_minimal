from django.contrib import admin

# Register your models here.
from store.models import Trade, Sku, Visit, Territory

admin.site.register(Visit)
admin.site.register(Trade)
admin.site.register(Sku)
admin.site.register(Territory)
