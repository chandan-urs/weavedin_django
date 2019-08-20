from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include
from django.urls import path


router = DefaultRouter()
router.register('branchs', views.BranchViewSet)
router.register('items', views.ItemViewSet)
router.register('variants', views.VariantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
