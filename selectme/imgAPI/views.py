from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import post_image


from .serializers import post_image_serializer


class post_image_view(APIView):
    # parser_class = (FileUploadParser,)
    def get(self, request, *args, **kwargs):
        data = post_image.objects.all()
        serializer = post_image_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        image_serializer = post_image_serializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
