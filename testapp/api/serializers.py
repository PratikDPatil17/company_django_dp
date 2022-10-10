from testapp.models import Company

from rest_framework.serializers import ModelSerializer

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"