from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        # return super().has_permission(request, view)
        return True
    
    def has_object_permission(self, request, view, obj):
        return obj.blog_owner == request.user