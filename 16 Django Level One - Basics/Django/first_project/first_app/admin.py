from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage, My_Roles, Users

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(My_Roles)
admin.site.register(Users)