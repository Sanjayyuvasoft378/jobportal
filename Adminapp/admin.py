from django.contrib import admin

from .models import AboutUs, CandidateInfo, CompanyInfo

# Register your models here.
admin.site.register(CandidateInfo)
admin.site.register(CompanyInfo)
admin.site.register(AboutUs)

