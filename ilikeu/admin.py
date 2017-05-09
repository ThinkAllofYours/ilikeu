from django.contrib import admin
from .models import MateDates
from .models import Human
# Register your models here.


class HumanAdmin(admin.ModelAdmin):
    model = Human
    list_display = ['mate_date', 'gender', 'mate_seq', 'phoneNumber', 'choice1', 'choice2']
    list_filter = ['mate_date']
    search_fields = ['phoneNumber']


admin.site.register(Human, HumanAdmin)
admin.site.register(MateDates)
