from django.contrib import admin

from .models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'company_text']

admin.site.register(Company)
