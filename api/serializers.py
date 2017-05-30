from rest_framework import serializers
from . import Task,Interface
import collections
import hashlib
import uuid
class JSONSerializerField(serializers.Field):
	def to_internal_value(self,data):
		return data
	def to_representation(self,value):
		return value


class InterfaceSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4,read_only=True)
    name=serializers.CharField(max_length=100)

class ConfigSerializer(serializers.Serializer):
    interface=InterfaceSerializer()
    def create(self, validated_data):
        return Interface(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    #config = JSONSerializerField()
    name=serializers.CharField(max_length=100)
    config=ConfigSerializer()
    def create(self, validated_data):
        validated_data['config']['interface']=Interface(**validated_data['config']['interface'])
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        print("updte: ",validated_data)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance