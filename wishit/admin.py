from django.contrib import admin
from wishit.models import *


class WishListAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)

#class UserAdmin(admin.ModelAdmin):
#	readonly_fields = ('id',)

#admin.site.register(User, UserAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Gift)


# Register your models here.

