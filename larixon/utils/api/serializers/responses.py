from rest_framework import serializers


class ResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class UUIDResponseSerializer(ResponseSerializer):
    id = serializers.UUIDField()

    def fail(self):
        super(UUIDResponseSerializer, self).fail()
