from rest_framework import permissions

class userOwnPermission(permissions.BasePermission):
    """Permissions"""
    
    def __has_permission__(self,request,view,obj):
        """Check if user has permission"""
        if(request.method in  permissions.SAFE_METHODS):
            return True
        return obj.id==request.user.idS    
        
        
class updateOwnStatus(permissions.BasePermission):
    """Permissions allow update own status"""
    def has_object_permission(self, request, view, obj):
        """check user update own status"""  
        
        if(request.method in  permissions.SAFE_METHODS):
            return True
        return obj.user_prfile.id==request.user.id   