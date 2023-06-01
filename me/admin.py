from django.contrib import admin
#from .models import Blog
from .models import  Customer
from .models import Blogg
from .models import billmount
from .models import exceldata
#from .models import customer
#from django.contrib.auth.admin import UserAdmin

#from .models import tbl_loginn

# Register your models here.
class CustomerAdmi(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmi)
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blogg, CustomerAdmin)
class bl(admin.ModelAdmin):
    pass
admin.site.register(billmount, bl)
class exdata(admin.ModelAdmin):
    pass
admin.site.register(exceldata, exdata)
#admin.site.register(Blog)
#admin.site.register(Blogg)
