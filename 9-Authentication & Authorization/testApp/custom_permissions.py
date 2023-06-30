from rest_framework import permissions 

class IsReadOnlyPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.method in permissions.SAFE_METHODS


class IsGETOrPATCHPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		ALLOWED_METHODS = ['GET', 'PATCH']
		return request.method in ALLOWED_METHODS
