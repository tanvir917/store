from django.urls import path
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('customers', views.CustomerViewSet, basename='customers')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

#URLConf
urlpatterns = router.urls  + products_router.urls

#urlpatterns += [
#     path('', include(router.urls)),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view()),
#]
