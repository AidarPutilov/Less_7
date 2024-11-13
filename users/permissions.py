from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Проверка принадлежности"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moders").exists()


# class IsOwner(BasePermission):

#     def has_object_permission(self, request, view, object):
#         if object.owner == request.user:
#             return True
#         return False
