import requests
from django.shortcuts import render

def get_geography_info(request):
	ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
	ip = '104.205.134.211'
	access_key = 'access_key=83393c0990ea76c7e0d9afa02e8a20ad'
	URL = f'http://api.ipstack.com/{ip}?{access_key}'

	response = requests.get(URL)
	data = response.json()
	return render(request, 'testapp/info.html', context=data)

