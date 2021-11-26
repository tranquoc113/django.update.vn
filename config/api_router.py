from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from myupdate.blog.views import CategoryViewSet, AuthInfor

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

print(settings.DEBUG)

router.register("category", CategoryViewSet, basename="category")
print('go----------')
urlpatterns = [
    path('', include(router.urls)),
    path('info/', AuthInfor.as_view())
]
# app_name = "api"
# urlpatterns = router.urls
