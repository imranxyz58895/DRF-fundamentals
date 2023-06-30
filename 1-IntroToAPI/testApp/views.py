import json

from . import mixins
from django.shortcuts import render, HttpResponse
from django.views.generic import View


def employee_data_HttpView(request):
    employee_data = {
        'no': 100,
        'name': 'Sunny Leone',
        'salary': 1000,
        'address': 'Mumbai',
    }

    response = f"""
    <ul>Employee Information
        <li>Id: {employee_data['no']}</li>
        <li>Name: {employee_data['name']}</li>
        <li>Salary: {employee_data['salary']}</li>
        <li>Address: {employee_data['address']}</li>
    </ul>
    """
    return HttpResponse(response)

def employee_data_JSONView(request):
    """
    json.loads(data) ► Decodes JSON data to Python dict
    json.dumps(dict) ► Decodes Python dict data to JSON
    Default HttpResponse is `content_type=text/html`
    """
    employee_data = {
        'no': 200,
        'name': 'Malaika Arora',
        'salary': 2000,
        'address': 'Pune',
    }

    json_data = json.dumps(employee_data, indent=3)
    return HttpResponse(json_data, content_type='application/json')


class JSONView(View):
    def get(self, request, *args, **kwargs):
        employee_data = {
            'no': 300,
            'name': 'Poonam Panday',
            'salary': 3000,
            'address': 'Nagpur',
        }

        json_data = json.dumps(employee_data, indent=3)
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({
            'msg': 'This is from Post method',
        }, indent=3)
        return HttpResponse(json_data, content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        json_data = json.dumps({
            'msg': 'This is from Put method',
        }, indent=3)
        return HttpResponse(json_data, content_type='application/json')

    def patch(self, request, *args, **kwargs):
        json_data = json.dumps({
            'msg': 'This is from Patch method',
        }, indent=3)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({
            'msg': 'This is from Delete method',
        }, indent=3)
        return HttpResponse(json_data, content_type='application/json')


class MixinResponse(View, mixins.HttpResponseMixin):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({
            'msg': 'This is from Get method',
        })

        return self.render_to_http_response(json_data)