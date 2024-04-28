import os

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer
from jinja2 import Template
from django.conf import settings
from django.http import HttpResponse


def index(request):
    print("+++++++++++++path=%s++++++++++++", os.path.join(settings.BASE_DIR, 'static','index.html'))
    with open(os.path.join(settings.BASE_DIR, 'static', 'index.html'), 'rb') as f:
        return HttpResponse(f.read(), content_type="text/html")


class RenderAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            tmpl = Template(serializer.validated_data['jinja_message'])
            result = tmpl.render(serializer.validated_data['context'])
            return Response({"result": result})
        return Response(serializer.errors, status=400)
