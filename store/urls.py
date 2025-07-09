from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from pprint import pprint

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

#URLConf
urlpatterns = router.urls

#urlpatterns += [
#     path('', include(router.urls)),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view()),
#]
