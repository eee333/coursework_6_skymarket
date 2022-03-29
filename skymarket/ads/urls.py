from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

ad_router = SimpleRouter()
comment_router = SimpleRouter()
ad_router.register("", AdViewSet, basename="ads")
comment_router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ad_router.urls)),
    path("<int:pk>/", include(comment_router.urls)),
]
