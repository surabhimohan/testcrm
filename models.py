from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ApiEndPoint(BaseModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(BaseModel):
    name = models.CharField(max_length=100)
    permission = models.ManyToManyField(ApiEndPoint)

    def __str__(self):
        return self.name


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Table(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class FieldList(BaseModel):
    FIELDS_LIST = [
        ("date", "Date"),
        ("dropdown", "Dropdown"),
        ("email", "Email"),
        ("file", "File"),
        ("image", "Image"),
        ("multi_dropdown", "Multi Dropdown"),
        ("phone", "Phone"),
        ("text", "Text"),
        ("user", "User")
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50, choices=FIELDS_LIST, default="TEXT")
    field_values = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.table.name +" | "+ self.name


class MasterData(BaseModel):
    field_name = models.ForeignKey(FieldList, on_delete=models.CASCADE)
    value = models.TextField()
    validate_value = models.TextField(blank=True, null=True)

    # this is not needed if small_image is created at set_image
    def save(self, *args, **kwargs):
        if self.field_name.field_type == "dropdown":
            if self.value in self.field_name.field_values.split(","):
                self.validate_value = self.value
            else:
                raise ValueError("Value not within allowed range")

        elif self.field_name.field_type == "user":
            if self.value in User.objects.all().values_list('id', flat=True):
                self.validate_value = self.value
            else:
                raise ValueError("User not present")

        elif self.field_name.field_type == "text":
            self.validate_value = self.value

        elif self.field_name.field_type == "phone":
            if self.value.isnumeric():
                self.validate_value = self.value
            else:
                raise ValueError("Phone can only contain numbers")
        else:
            self.validate_value = None
        super(MasterData, self).save(*args, **kwargs)