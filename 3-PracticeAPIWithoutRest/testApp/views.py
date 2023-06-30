import json
from testApp import models, forms, mixins, utilites

from django.shortcuts import render, HttpResponse
from django.core.serializers import serialize 
from django.utils.decorators import method_decorator
from django.views.generic import View 
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class CelebrityView(View, mixins.SerializerMixin):
    def get(self, request, *args, **kwargs):
        celebrities = models.Celebrity.objects.all()
        celebrities_json_data = self.serialize_to_json(celebrities)
        return HttpResponse(celebrities_json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body

        is_valid = utilites.validate_json(data)
        if not is_valid:
            message = json.dumps({
                'message': 'Invalid Json data'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')

        new_data = json.loads(data)
        form = forms.CelebrityModelForm(new_data)

        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({
                'message': 'New Celebrity Added'
            }, indent=3), content_type='application/json')
        
        if form.errors:
            return HttpResponse(json.dumps({
                'message': 'Something went wrong, try again'
            }, indent=3), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class CelebrityDetailView(View, mixins.SerializerMixin):
    def get(self, request, pk, *args, **kwargs):
        try:
            celebrity = models.Celebrity.objects.get(id=pk)
        except models.Celebrity.DoesNotExist as error:
            return HttpResponse(json.dumps({
                'message': 'Invalid Id request'
            }, indent=3), content_type='application/json')
        
        celebrity_json_data = self.serialize_to_json([celebrity])
        return HttpResponse(celebrity_json_data, content_type='application/json')

    def put(self, request, pk, *args, **kwargs):
        try:
            celebrity = models.Celebrity.objects.get(id=pk)
        except models.Celebrity.DoesNotExist as error:
            return HttpResponse(json.dumps({
                'message': 'Invalid Id request'
            }, indent=3), content_type='application/json')

        data = request.body

        is_valid = utilites.validate_json(data)
        if not is_valid:
            message = json.dumps({
                'message': 'Invalid Json data'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')

        requested_data = json.loads(data)
        original_data = {
            'unique_no': celebrity.unique_no,
            'name': celebrity.name,
            'net_worth': celebrity.net_worth,
            'address': celebrity.address,
        }
        original_data.update(requested_data)

        form = forms.CelebrityModelForm(original_data, instance=celebrity)

        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({
                'message': 'Updated Successfully'
            }, indent=3), content_type='application/json')
        
        if form.errors:
            return HttpResponse(json.dumps({
                'message': 'Something went wrong, try again'
            }, indent=3), content_type='application/json')
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            celebrity = models.Celebrity.objects.get(id=pk)
        except models.Celebrity.DoesNotExist as error:
            return HttpResponse(json.dumps({
                'message': 'Invalid Id request'
            }, indent=3), content_type='application/json')
        
        status, deleted_item = celebrity.delete() 
        if status:
            return HttpResponse(json.dumps({
                'message': 'Requested Celebrity is deleted'
            }, indent=3), content_type='application/json')
        else:
            return HttpResponse(json.dumps({
                'message': 'Invalid request'
            }, indent=3), content_type='application/json')
