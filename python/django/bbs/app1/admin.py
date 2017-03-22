from django.contrib import admin
from app1 import models


class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'view_count', 'created_at')  # 后台显示的字段
    list_filter = ('created_at', )  # 按创建时间过滤
    search_fields = ('title',)  # 搜索

admin.site.register(models.BBSUser)
admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
