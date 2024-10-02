from django.urls import path

from app_merchant.views.merchant import MerchantCreateAPIView, MerchantRetrieveAPIView, MerchantUpdateAPIView, \
    MerchantDestroyAPIView

urlpatterns = [
    path('merchants/', MerchantCreateAPIView.as_view(), name='merchant-create'),
    path('merchants/<int:pk>/', MerchantRetrieveAPIView.as_view(), name='merchant-detail'),
    path('merchants/<int:pk>/update/', MerchantUpdateAPIView.as_view(), name='merchant-update'),
    path('merchants/<int:pk>/delete/', MerchantDestroyAPIView.as_view(), name='merchant-delete'),

]
