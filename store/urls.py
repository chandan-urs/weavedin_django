from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include
from django.urls import path


router = DefaultRouter()
router.register('branch', views.BranchViewSet)
router.register('item', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
