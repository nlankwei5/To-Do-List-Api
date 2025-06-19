from rest_framework import permissions


class IsOwnerPermissions (permissions.BasePermission):
    message = "Permission denied! You can edit or delete another User's To-do"

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.user == request.user 
        return False 