import json
from . import models, forms, mixins

from django.shortcuts import render, HttpResponse
from django.core.serializers import serialize 
from django.utils.decorators import method_decorator
from django.views.generic import View 
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class CelebrityView(View, mixins.SerializeMixin):
    def get(self, request, *args, **kwargs):
        received_data = request.body # b'{}'

        def validate_json(data):
            try:
                if json.loads(data):
                    return True
            except json.JSONDecodeError as error: 
                return False
        
        if not validate_json(received_data):
            message = json.dumps({
                'message': 'Invalid JSON data, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        decodes_json_data = json.loads(received_data)
        ID = decodes_json_data.get('id', None)

        if ID is None:
            Celebrities = models.Celebrity.objects.all()
            serialized_data = self.serialize_to_json(Celebrities)
            return HttpResponse(serialized_data, content_type='application/json')

        try:
            Celebrity = models.Celebrity.objects.get(id=ID)
        except models.Celebrity.DoesNotExist as error:
            return HttpResponse(json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3), content_type='application/json')
        
        serialized_data = self.serialize_to_json([Celebrity])
        return HttpResponse(serialized_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        received_data = request.body # b'{key: value}'

        def validate_json(data):
            try:
                if json.loads(data):
                    return True
            except json.JSONDecodeError as error: 
                return False
        
        if not validate_json(received_data):
            message = json.dumps({
                'message': 'Invalid JSON data, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        decodes_json_data = json.loads(received_data)
        form = forms.CelebrityModelForm(decodes_json_data)

        if form.is_valid():
            form.save()
            message = json.dumps({
                'message': 'Celebrity added successfully'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')

        if form.errors:
            return HttpResponse(json.dumps({'message': form.errors}), content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        received_data = request.body # b'{key: value}'

        def validate_json(data):
            try:
                if json.loads(data):
                    return True
            except json.JSONDecodeError as error: 
                return False
        
        if not validate_json(received_data):
            message = json.dumps({
                'message': 'Invalid JSON data, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        decodes_json_data = json.loads(received_data)
        ID = decodes_json_data.get('id', None)

        if ID is None:
            return HttpResponse(json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3), content_type='application/json')

        try:
            Celebrity = models.Celebrity.objects.get(id=ID)
        except models.Celebrity.DoesNotExist as error:
            return HttpResponse(json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3), content_type='application/json')

        celebrity_data = {
            'unique_no': Celebrity.unique_no,
            'name': Celebrity.name,
            'net_worth': Celebrity.net_worth,
            'address': Celebrity.address,
        }
        celebrity_data.update(decodes_json_data)
        form = forms.CelebrityModelForm(celebrity_data, instance=Celebrity)

        if form.is_valid():
            form.save()
            message = json.dumps({
                'message': 'Celebrity Info Updated successfully'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')

        if form.errors:
            return HttpResponse(json.dumps({'message': form.errors}), content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        received_data = request.body

        def validate_json(data):
            try:
                if json.loads(data):
                    return True
            except json.JSONDecodeError as error: 
                return False
        
        if not validate_json(received_data):
            message = json.dumps({
                'message': 'Invalid JSON data, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')

        decodes_json_data = json.loads(received_data)
        ID = decodes_json_data.get('id', None)

        if ID is None:
            return HttpResponse(json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3), content_type='application/json')

        try:
            Celebrity = models.Celebrity.objects.get(id=ID)
        except models.Celebrity.DoesNotExist as error:
            return HttpResponse(json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3), content_type='application/json')
        
        status, deleted_item = Celebrity.delete()

        if status:
            return HttpResponse(json.dumps({
                'message': 'Deleted Successfully'
            }, indent=3), content_type='application/json')
        else:
            return HttpResponse(json.dumps({
                'message': 'Something went wrong!, Try again'
            }, indent=3), content_type='application/json')
