from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):

    def validate_company_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                'Company name must be at least 5 characters'
            )
        return value

    class Meta:
        model = Company
        fields = '__all__'
