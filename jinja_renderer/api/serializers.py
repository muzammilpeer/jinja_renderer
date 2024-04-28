from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    jinja_message = serializers.CharField()
    context = serializers.DictField()
