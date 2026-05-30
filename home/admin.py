from django.contrib import admin

# Register your models here.

from .import models

admin.site.register(models.Blog)
admin.site.register(models.Subscription)
admin.site.register(models.SubscriptionOrder)

