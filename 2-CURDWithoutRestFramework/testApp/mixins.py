import json
from django.core.serializers import serialize


class SerializerMixin:
    def serialize_to_json(self, queryset):
        list_of_data = json.loads(serialize('json', queryset))

        data_fields = []
        for data in list_of_data:
            data_fields.append(data['fields'])

        return json.dumps(data_fields, indent=3)
        