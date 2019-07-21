from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import Translation, Source
from .serializers import TranslationsSerializer

class ListCreateTranslationView(generics.ListCreateAPIView):
  """
  GET songs/
  POST songs/
  """
  queryset = Translation.objects.all()
  serializer_class = TranslationsSerializer

  def post(self, request, *args, **kwargs):
    createdSource = Source.objects.create(
      author=request.data['source']['author'],
      url=request.data['source']['url']
    )
    createdTranslation = Translation.objects.create(
      text=request.data['text'],
      translation=request.data['translation'],
      source=createdSource
    )
    return Response(
      data=TranslationsSerializer(createdTranslation).data,
      status=status.HTTP_201_CREATED
    )
