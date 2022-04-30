from django.contrib import admin
from .models import *


# admin.site.register(AssignedTo)
# admin.site.register(Area)
# admin.site.register(Builder)
# admin.site.register(City)
# admin.site.register(Country)
# admin.site.register(SubCommunity)
# admin.site.register(Project)
#
# admin.site.register(Facing)
# admin.site.register(FinancialStatus)
# admin.site.register(ForName)
# admin.site.register(ProjectStatus)
# admin.site.register(PropertyType)
# admin.site.register(PropertiesStatus)
# admin.site.registennnr(Occupancy)
# admin.site.register(RenovationType)
# admin.site.register(Type)
# admin.site.register(TypeOfFurnishing)
# admin.site.register(TenureOfProperty)
# admin.site.register(Properties)

admin.site.register(Company)

@admin.register(ApiEndPoint)
class ApiEndPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(MasterData)
class MasterDataAdmin(admin.ModelAdmin):
    list_display = ("field_name", 'value', 'validate_value')

admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Table)
admin.site.register(FieldList)


