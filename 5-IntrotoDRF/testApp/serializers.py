from . import models
from rest_framework import serializers

    # built in validator's function - 1
def multiples_by_100(value):
    if value % 100 != 0:
        raise serializers.ValidationError('Must be multiplied by 0')

    return value


class CelebrityModelSerializer(serializers.Serializer):
    unique_no = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    net_worth = serializers.FloatField(validators=[multiples_by_100])
    address = serializers.CharField(max_length=200)

        # Field level validation - 2
    def validate_net_worth(self, bucks):
        if bucks < 5000:
            raise serializers.ValidationError('Net worth must be bigger $100000')
        return bucks

        # Object level validation - 3
    def validate(self, data): # data=OrderedDict()
        name = data.get('name')
        net_worth = data.get('net_worth')

        if name.split()[0].lower() == 'sunny' and net_worth < 5000:
            raise serializers.ValidationError('Must be > $5K')
        
        return data

    def create(self, validated_data):
        return models.Celebrity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.unique_no = validated_data.get('unique_no', instance.unique_no)
        instance.name = validated_data.get('name', instance.name)
        instance.net_worth = validated_data.get('net_worth', instance.net_worth)
        instance.address = validated_data.get('address', instance.address)

        instance.save()
        return instance