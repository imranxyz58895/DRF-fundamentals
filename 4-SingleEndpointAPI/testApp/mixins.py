import json 
from django.core.serializers import serialize 


class SerializeMixin:
    def serialize_to_json(self, queryset):
        list_of_data = json.loads(serialize('json', queryset))

        fields = []
        for obj in list_of_data:
            fields.append(obj['fields'])

        return json.dumps(fields, indent=3)