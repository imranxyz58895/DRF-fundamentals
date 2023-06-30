import json
from . import mixins, models, forms 

from django.shortcuts import render, HttpResponse
from django.views.generic import View # https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/
from django.core.serializers import serialize # https://docs.djangoproject.com/en/4.1/topics/serialization/
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



@method_decorator(csrf_exempt, name='dispatch')
class EmployeDetailView(View, mixins.SerializerMixin):
    def get(self, request, pk, *args, **kwargs):
        try:
            employee = models.Employee.objects.get(id=pk)
        except models.Employee.DoesNotExist as error:
            employee_detail = json.dumps({
                'id': 'Invalid Id'
            })
        else:
            employee_detail = self.serialize_to_json([employee])

        return HttpResponse(employee_detail, content_type='application/json')

        # employee_details = {
        #     'no': employee.no,
        #     'name': employee.name,
        #     'salary': employee.salary,
        #     'address': employee.address
        # }
        # return HttpResponse(json.dumps(employee_details, indent=3), content_type='application/json')

        # django serialization
        # employee_details_json = serialize('json', [employee], fields=('no', 'name', 'salary'))
        # return HttpResponse(employee_details_json, content_type='application/json')
        
        # with the help of mixin
        # employee_detail = self.serialize_to_json([employee])
        # return HttpResponse(employee_detail, content_type='application/json')

    def put(self, request, pk, *args, **kwargs):
        # utility function
        def get_databy_id(pk):
            try:
                employee = models.Employee.objects.get(id=pk)
            except models.Employee.DoesNotExist as error:
                employee = None
            return employee

        employee_data = get_databy_id(pk)
        if employee_data is None:
            message = {
                'msg': 'Invalid Request'
            }
            return HttpResponse(json.dumps(message), content_type='application/json')  

        data = request.body 

        # utility function
        def validate_json(data):
            try:
                if json.loads(data):
                    return True
            except json.JSONDecodeError as error: 
                return False

        is_valid = validate_json(data)
        if not is_valid:
            # utility function
            message = {
                'msg': 'Invalid Request'
            }
            return HttpResponse(json.dumps(message), content_type='application/json')

        original_data = {
            'no': employee_data.no,
            'name': employee_data.name,
            'address': employee_data.address,
            'salary': employee_data.salary,
        }
        original_data.update(json.loads(data))

        form = forms.EmployeeModelForm(original_data, instance=employee_data)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'msg': 'Updated Successfully'}), content_type='application/json')
        
        if form.errors:
            return HttpResponse(json.dumps({'msg': form.errors}), content_type='application/json')

    def delete(self, request, pk, *args, **kwargs):
        # utility function
        def get_databy_id(pk):
            try:
                employee = models.Employee.objects.get(id=pk)
            except models.Employee.DoesNotExist as error:
                employee = None
            return employee

        employee_data = get_databy_id(pk)
        if employee_data is None:
            message = {
                'msg': 'Invalid Request'
            }
            return HttpResponse(json.dumps(message), content_type='application/json')  

        status, deleted_item = employee_data.delete()
        print(status, deleted_item) # (1, {'test.Employee': 1})

        if status == 1:
            message = {
                'msg': 'Deleted Successfully'
            }
            return HttpResponse(json.dumps(message), content_type='application/json') 
        else:
            message = {
                'msg': 'Something is Wrong, try again'
            }
            return HttpResponse(json.dumps(message), content_type='application/json') 


@method_decorator(csrf_exempt, name='dispatch')
class EmployeesView(View):
    def get(self, request, *args, **kwargs):
        employees = models.Employee.objects.all()
        employee_serializers = serialize('json', employees)
        return HttpResponse(employee_serializers, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        data = request.body

        def validate_json(data):
            try:
                if json.loads(data):
                    return True
            except json.JSONDecodeError as error: 
                return False

        is_valid = validate_json(data)
        if not is_valid:
            message = {
                'msg': 'Invalid Request'
            }
            return HttpResponse(json.dumps(message), content_type='application/json')

        form = forms.EmployeeModelForm(json.loads(data))
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'msg': 'Added Successfully'}), content_type='application/json')
        
        if form.errors:
            return HttpResponse(json.dumps({'msg': form.errors}), content_type='application/json')
    
    
class EmployeeFieldsView(View, mixins.SerializerMixin):
    def get(self, request, *args, **kwargs):
        employees = models.Employee.objects.all()
        """
        list_of_employees = json.loads(serialize('json', employees))

        employee_fields = []
        for data in list_of_employees:
            employee_fields.append(data['fields'])

        employee_serializers = json.dumps(employee_fields, indent=3)
        """
        employee_serializers = self.serialize_to_json(employees)
        return HttpResponse(employee_serializers, content_type='application/json')
