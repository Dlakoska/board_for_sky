from rest_framework import permissions


class IsAdminOrAuthor(permissions.BasePermission):
    """
    Проверяет, является ли пользователь администратором или автором.
    """

    def has_object_permission(self, request, view, obj):

        if request.user.role:
            return True

        return obj.author == request.user
