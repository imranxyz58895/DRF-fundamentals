import json
from django.core.serializers import serialize 

class SerializerMixin(object):
    def serialize_to_json(self, query_set):
        data = serialize('json', query_set)
        list_of_data = json.loads(data)

        fields = []
        for data in list_of_data:
            fields.append(data['fields'])
        
        return json.dumps(fields, indent=3)