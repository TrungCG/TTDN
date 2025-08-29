from django.contrib import admin

from .models import ProvinceOld, District, CommuneOld, ProvinceNew, CommuneNew, CommuneHistory

admin.site.register(ProvinceOld)
admin.site.register(District)
admin.site.register(CommuneOld)
admin.site.register(ProvinceNew)
admin.site.register(CommuneNew)
admin.site.register(CommuneHistory)