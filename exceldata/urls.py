from django.contrib import admin
from django.urls import path,include
from api.views import Studentview
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('student',Studentview)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(router.urls))
]
