from rest_framework.viewsets import ModelViewSet

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from testapp.api.serializers import CompanySerializer

from testapp.models import Company

class RESTapiCRUDView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]
    authentication_classes = [JSONWebTokenAuthentication,]
