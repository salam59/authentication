from rest_framework import permissions


class ClientPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.user_type == 'client' and view.action != 'create'
    
    def has_object_permission(self, request, view, obj):
        #as has_permission checks for client or not no need to check again
        return request.user == obj
    

class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'admin'