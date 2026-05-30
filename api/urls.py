from rest_framework.routers import DefaultRouter
from django.urls import path, include
from home import views


router = DefaultRouter()
router.register(r'blog',views.BlogView,basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = router.urls
