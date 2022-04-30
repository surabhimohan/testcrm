# from django.db import models
#
#
# class BaseModel(models.Model):
#     # company = models.CharField(max_length=500)
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
#
# class AssignedTo(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class Builder(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class Country(BaseModel):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class City(BaseModel):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#
#
# class Area(BaseModel):
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#
#
# class SubCommunity(BaseModel):
#     area = models.ForeignKey(Area, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#
#
# class Project(BaseModel):
#     # Project Details
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     area = models.ForeignKey(Area, on_delete=models.CASCADE)
#     street = models.CharField(max_length=1000, null=True, blank=True)
#     sub_community = models.ForeignKey(SubCommunity, on_delete=models.SET_NULL, null=True, blank=True)
#     co_ordinates = models.CharField(max_length=500, null=True, blank=True)
#     property = models.CharField(max_length=500, null=True, blank=True)
#     assigned_to = models.ForeignKey(AssignedTo, on_delete=models.CASCADE)
#     tower = models.CharField(max_length=500, null=True, blank=True)
#     builder = models.ForeignKey(Builder, on_delete=models.SET_NULL, null=True, blank=True)
#     name = models.CharField(max_length=500)
#     # Description Details
#     description = models.TextField(null=True, blank=True)
#
#
# class Facing(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class FinancialStatus(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class ForName(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class ProjectStatus(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class PropertyType(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class PropertiesStatus(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class Occupancy(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class RenovationType(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class Type(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class TypeOfFurnishing(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class TenureOfProperty(BaseModel):
#     name = models.CharField(max_length=500)
#
#
# class Properties(BaseModel):
#     # Basic Information : project includes: project name, country, area, city, sub-community, street, builder
#     project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
#
#     # Custom Information
#     type = models.ForeignKey(Type, on_delete=models.CASCADE)
#     floor_number = models.CharField(max_length=500, null=True, blank=True)
#     for_name = models.ForeignKey(ForName, on_delete=models.CASCADE)
#     project_status = models.ForeignKey(ProjectStatus, on_delete=models.SET_NULL, null=True, blank=True)
#     property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
#     plot_size = models.CharField(max_length=500, null=True, blank=True)
#     bed_rooms = models.CharField(max_length=10)
#     bathrooms = models.CharField(max_length=10, null=True, blank=True)
#     built_up_area = models.CharField(max_length=500, null=True, blank=True)
#     layout_type = models.CharField(max_length=500, null=True, blank=True)
#     no_of_parking = models.CharField(max_length=500, null=True, blank=True)
#     square_feet = models.CharField(max_length=500)
#     created_by = models.CharField(max_length=500, null=True, blank=True)
#
#     type_of_furnishing = models.ForeignKey(TypeOfFurnishing, on_delete=models.SET_NULL, null=True, blank=True)
#     occupancy = models.ForeignKey(Occupancy, on_delete=models.SET_NULL, null=True, blank=True)
#     tenure_of_property = models.ForeignKey(TenureOfProperty, on_delete=models.SET_NULL, null=True, blank=True)
#     mail_id = models.CharField(max_length=500, null=True, blank=True)
#     renovation_type = models.ForeignKey(RenovationType, on_delete=models.SET_NULL, null=True, blank=True)
#     agency_reference = models.CharField(max_length=500, null=True, blank=True)
#     build_year = models.IntegerField(blank=True, null=True)
#     building_age = models.CharField(max_length=500, null=True, blank=True)
#     assigned_to = models.ForeignKey(AssignedTo, on_delete=models.CASCADE)
#     availability_of_possession = models.DateField(null=True, blank=True)
#     properties_status = models.ForeignKey(PropertiesStatus, on_delete=models.CASCADE)
#
#     # Features
#     views = models.CharField(max_length=500, null=True, blank=True)
#     facing = models.ForeignKey(Facing, on_delete=models.SET_NULL, null=True, blank=True)
#     amenities = models.CharField(max_length=500, null=True, blank=True)
#
#     # Description Details
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#
#     # Registration Details
#     rera_number = models.CharField(max_length=500)
#     rera_permit_issue_date = models.DateField(null=True, blank=True)
#     rera_permit_expiry_date = models.DateField(null=True, blank=True)
#     dewa_number = models.CharField(max_length=500, null=True, blank=True)
#     dewa_permit_number = models.CharField(max_length=500, null=True, blank=True)
#     dtcm_permit_number = models.CharField(max_length=500, null=True, blank=True)
#     trakheesi_permit_number = models.CharField(max_length=500, null=True, blank=True)
#
#     # Payment Information
#     price = models.CharField(max_length=500, null=True, blank=True)
#     duration = models.IntegerField(blank=True, null=True)
#     application_price = models.CharField(max_length=500, null=True, blank=True)
#     maintenance_charges = models.CharField(max_length=500, null=True, blank=True)
#     currency = models.CharField(max_length=500, null=True, blank=True)
#     financial_status = models.ForeignKey(FinancialStatus, on_delete=models.SET_NULL, null=True, blank=True)
#     no_of_cheques = models.IntegerField(blank=True, null=True)
#
#     # Profile Picture
#     properties_images = models.ImageField(blank=True, upload_to='properties_images')
#     floor_plan = models.ImageField(blank=True, upload_to='properties_images')
#     brochure = models.FileField(blank=True, upload_to='properties_images')
#     youtube_link = models.CharField(max_length=500, null=True, blank=True)
#     degree_view_360 = models.CharField(max_length=500, null=True, blank=True)
#
#     # Feeds for Property Market Place
#     property_finder = models.CharField(max_length=500, null=True, blank=True)
#     bayut = models.CharField(max_length=500, null=True, blank=True)
#     zoom = models.CharField(max_length=500, null=True, blank=True)
#     dubizzle = models.CharField(max_length=500, null=True, blank=True)
#
#     # Properties Portal Details
#     property_crm_status = models.CharField(max_length=500, null=True, blank=True)
#     verified_listing = models.CharField(max_length=500, null=True, blank=True)
