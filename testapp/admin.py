from django.contrib import admin

from testapp.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "total_emp", "address"]

admin.site.register(Company, CompanyAdmin)

