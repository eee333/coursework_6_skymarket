from django.urls import include, path

# настройка роутов для модели
from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet

ad_router = routers.SimpleRouter()
ad_router.register(r"ads", AdViewSet, basename="ads")

comment_router = routers.NestedSimpleRouter(ad_router, r"ads", lookup="ad")
comment_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ad_router.urls)),
    path("", include(comment_router.urls)),
]
