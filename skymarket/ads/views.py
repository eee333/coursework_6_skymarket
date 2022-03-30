from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    # permission_classes = [ReadOnlyOrAdminPermissionList]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AdDetailSerializer
        return AdSerializer


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the comments for
        the ad.
        """
        ad = self.kwargs['pk']
        return Comment.objects.filter(ad=ad)

    def perform_create(self, serializer):
        ad = self.kwargs['pk']
        serializer.save(author=self.request.user)
        serializer.save(ad_id=ad)
