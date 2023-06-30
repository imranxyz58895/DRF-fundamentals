from django.contrib.auth.models import User
from rest_framework import authentication, exceptions 


class CustomAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		username = request.GET.get('username')

		if username is not None:
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist as error:
				raise exceptions.AuthenticationFailed('Invalid credentials')
			else:
				return (user, None)
		else:
			return None 



