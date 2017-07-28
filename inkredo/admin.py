from django.contrib import admin
from users.models import Users
from company.models import Company

admin.site.register(Users)
admin.site.register(Company)