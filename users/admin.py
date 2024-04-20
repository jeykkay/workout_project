from django.contrib import admin

from users.models import CustomUser, Trainer


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_num', )
    search_fields = ('first_name', 'last_name', )


admin.site.register(Trainer)
