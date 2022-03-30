# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions


class ListOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action == 'list':
                return True
            else:
                return False
        else:
            return True
