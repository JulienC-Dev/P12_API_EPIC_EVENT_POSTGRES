from rest_framework import permissions


class CustomEmployeePermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        print(bool(request.user))
        return bool(request.user and request.user.is_authenticated)


class CustomClientPermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
        if request.method == "PUT" or request.method == "DELETE" or request.method == "GET":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.method == "PUT":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
            if obj is not None and obj.employee == request.user:
                return True
        if request.method == "DELETE":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
            if obj is not None and obj.employee == request.user:
                return True
        return False


class CustomContractPermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
        if request.method == "PUT" or request.method == "DELETE" or request.method == "GET":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.method == "PUT":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
            if obj is not None and obj.client.employee == request.user:
                return True
        if request.method == "DELETE":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
            if obj is not None and obj.client.employee == request.user:
                return True
        return False


class CustomEvenementPermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        if request.method == "POST":
            return False
        if request.method == "PUT" or request.method == "DELETE" or request.method == "GET":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.method == "PUT":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
            if obj is not None and obj.employee == request.user:
                return True
        if request.method == "DELETE":
            if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True or \
                    request.user.groups.filter(name='groupe de vente').exists():
                return True
            if obj is not None and obj.employee == request.user:
                return True
        return False


