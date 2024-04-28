from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from jinja2 import Template

class RenderAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            tmpl = Template(serializer.validated_data['jinja_message'])
            result = tmpl.render(serializer.validated_data['context'])
            return Response({"result": result})
        return Response(serializer.errors, status=400)
