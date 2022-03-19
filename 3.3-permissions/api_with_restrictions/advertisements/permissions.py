from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Get запрос на чтение, поэтому все пользователи могут
        if request.method == 'GET':
            return True
        return request.user == obj.creator