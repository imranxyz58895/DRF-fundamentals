from . import models, serializers
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet 
from rest_framework.response import Response 


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        COLORS = [
            'Green',
            'Red',
            'Yellow',
        ]
        # it converts dictionary into JSON object
        return Response(data={
            'message': "Happy Pongal",
            'colors': COLORS,
        })

    def post(self, request, *args, **kwargs):
        parsed_data = serializers.TestSerializer(data=request.data)
        
        if parsed_data.is_valid():
            name = parsed_data.data.get('name', None)
            message = {
                f'Hello {name}, Happy Pongal!!'
            }
            return Response(data=message)
        else:
            return Response(data=parsed_data.errors)

    def put(self, request, *args, **kwargs):
        message = {
            'msg': 'This response is from Put request'
        }
        return Response(data=message)
    
    def patch(self, request, *args, **kwargs):
        message = {
            'msg': 'This response is from Patch request'
        }
        return Response(data=message)
    
    def delete(self, request, *args, **kwargs):
        message = {
            'msg': 'This response is from Delete request'
        }
        return Response(data=message)


class TestViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        COLORS = [
            'Green',
            'Red',
            'Yellow',
        ]
        # it converts dictionary into JSON object
        return Response(data={
            'message': "Happy Pongal",
            'colors': COLORS,
        })

    def create(self, request, *args, **kwargs):
        parsed_data = serializers.TestSerializer(data=request.data)
        
        if parsed_data.is_valid():
            name = parsed_data.data.get('name', None)
            message = {
                f'Hello {name}, Happy Pongal!!'
            }
            return Response(data=message)
        else:
            return Response(data=parsed_data.errors)

    def update(self, request, pk=None, *args, **kwargs):
        message = {
            'msg': 'This response is from Update request'
        }
        return Response(data=message)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        message = {
            'msg': 'This response is from Partial_Update request'
        }
        return Response(data=message)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        message = {
            'msg': 'This response is from destroy request'
        }
        return Response(data=message)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        message = {
            'msg': 'This response is from retrieve request'
        }
        return Response(data=message)