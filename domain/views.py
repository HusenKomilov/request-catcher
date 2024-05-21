from rest_framework import generics
from rest_framework.response import Response
from domain import serializers
from domain.utils import send_info


class RequestsCatcherView(generics.GenericAPIView):
    serializer_class = serializers.RequestCarcherView

    @send_info
    def get(self, request, *args, **kwargs):

        return Response({"message": "ok"})

    @send_info
    def put(self, request, *args, **kwargs):
        print("put request")
        return Response({"message": "ok"})

    @send_info
    def post(self, request, *args, **kwargs):
        print(request.heanders)
        return Response({"message": "ok"})
