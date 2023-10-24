from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Права доступа для модератора"""
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsOwner(BasePermission):
    """Права доступа для владельца"""
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class CoursePermission(BasePermission):
    """Права доступа для модератора и владельца"""
    def has_permission(self, request, view):
        if request.user.is_staff and request.method.upper() in ['DELETE', 'POST']:
            return False
        elif request.user.is_staff and request.method.upper() not in ['DELETE', 'POST']:
            return True
        return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        else:
            CoursePermission.message = 'Вы не являетесь владельцем'
            return False
