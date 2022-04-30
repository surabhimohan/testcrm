from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'


class FieldListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldList
        fields = '__all__'