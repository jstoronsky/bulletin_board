from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'У пользователя нет прав доступа'

    def has_permission(self, request, view):
        if request.user.role in ['Admin', 'admin']:
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False
