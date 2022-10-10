from django.contrib import admin
from django.urls import path, include

# from testapp import views

from rest_framework import routers
router = routers.DefaultRouter()

from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token, refresh_jwt_token

from testapp.api.views import RESTapiCRUDView

router.register("rest", RESTapiCRUDView, basename="rest")

urlpatterns = [
    path("", include(router.urls)),
    path("jwt_obtain/", obtain_jwt_token),
    path("jwt_verify/", verify_jwt_token),
    path("jwt_refresh/", refresh_jwt_token),

]