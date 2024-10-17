from rest_framework.routers import DefaultRouter
from .views import ItemViewSet #Items, GetUpdateItem
from django.urls import path

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('items/', Items.as_view(), name='addItem'),
#     path('items/<int:pk>', GetUpdateItem.as_view(), name='getUpdateItem'),
# ]