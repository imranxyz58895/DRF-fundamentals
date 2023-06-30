import json
import io
from . import models, serializers

from django.views.generic import View 
from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@method_decorator(csrf_exempt, name='dispatch')
class CelebrityCURDView(View):
    def get(self, request, *args, **kwargs):
        received_data = request.body

        # validating json data
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
        
        # decodes_data = json.loads(received_data)
        stream = io.BytesIO(received_data)
        decodes_data = JSONParser().parse(stream)
        ID = decodes_data.get('id', None)

        if ID is None:
            celebrities = models.Celebrity.objects.all()
            serializer = serializers.CelebrityModelSerializer(instance=celebrities, many=True)
            render_into_json = JSONRenderer().render(data=serializer.data)
            return HttpResponse(render_into_json, content_type='application/json')
        
        try:
            celebrity = models.Celebrity.objects.get(id=ID)
        except models.Celebrity.DoesNotExist as error:
            message = json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        serializer = serializers.CelebrityModelSerializer(instance=celebrity)
        render_into_json = JSONRenderer().render(data=serializer.data)
        return HttpResponse(render_into_json, content_type='application/json')

    # to add data in database create `create(validated_data)` method inside the serializer.
    def post(self, request, *args, **kwargs):
        received_data = request.body

        # validating json data
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
        
        stream = io.BytesIO(received_data)
        decodes_data = JSONParser().parse(stream)

        deserialized_data = serializers.CelebrityModelSerializer(data=decodes_data)
        if deserialized_data.is_valid():
            deserialized_data.save() # it calls create() method

        message = json.dumps({
                'message': 'Celebrity added successfully'
            }, indent=3)
        return HttpResponse(message, content_type='application/json')

    # to update data in database create `update(instance, validated_data)` method inside the serializer.
    def put(self, request, *args, **kwargs):
        received_data = request.body

        # validating json data
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
        
        stream = io.BytesIO(received_data)
        decodes_data = JSONParser().parse(stream)

        ID = decodes_data.get('id', None)
        if ID is None:
            message = json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        try:
            celebrity = models.Celebrity.objects.get(id=ID)
        except models.Celebrity.DoesNotExist as error:
            message = json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        deserialized_data = serializers.CelebrityModelSerializer(instance=celebrity, data=decodes_data, partial=True)

        if deserialized_data.is_valid():
            deserialized_data.save() # it calls update() method
            message = json.dumps({
                    'message': 'Celebrity info updated successfully'
                }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        if deserialized_data.errors:
            message = json.dumps(deserialized_data.errors, indent=3)
            return HttpResponse(message, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        received_data = request.body

        # validating json data
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
        
        stream = io.BytesIO(received_data)
        decodes_data = JSONParser().parse(stream)

        ID = decodes_data.get('id', None)
        if ID is None:
            message = json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        
        try:
            celebrity = models.Celebrity.objects.get(id=ID)
        except models.Celebrity.DoesNotExist as error:
            message = json.dumps({
                'message': 'Invalid ID request, try again'
            }, indent=3)
            return HttpResponse(message, content_type='application/json')
        else:
            celebrity.delete()
            message = json.dumps({
                    'message': 'Celebrity deleted successfully'
                }, indent=3)
            return HttpResponse(message, content_type='application/json')


        

