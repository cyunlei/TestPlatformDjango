from django.contrib import admin
from apitest.models import ApiTest, ApiStep, Apis


# Register your models here.

class ApiStepAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimetod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'Apitest']
    model = ApiStep
    extra = 1


class ApiTestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApiStepAdmin]


admin.site.register(ApiTest, ApiTestAdmin)


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimetod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']


admin.site.register(Apis)
