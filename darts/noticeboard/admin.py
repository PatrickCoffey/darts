from django.contrib import admin

from noticeboard.models import Notice

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notice, NoticeAdmin)