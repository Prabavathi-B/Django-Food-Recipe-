from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from Recipe.models import breakfast_details,dinner_details,juice_details,lunch_details,sweet_details


# Register your models here.

class VideoAdminMixin(AdminVideoMixin,admin.ModelAdmin):
    pass

admin.site.register(breakfast_details,VideoAdminMixin)
admin.site.register(dinner_details,VideoAdminMixin)
admin.site.register(juice_details,VideoAdminMixin)
admin.site.register(lunch_details,VideoAdminMixin)
admin.site.register(sweet_details,VideoAdminMixin)