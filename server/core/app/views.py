from django.shortcuts import render
from django.db.utils import IntegrityError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import Translation, Source
from .serializers import TranslationsSerializer

class ListCreateTranslationView(generics.ListCreateAPIView):

  queryset = Translation.objects.all()
  serializer_class = TranslationsSerializer

  def post(self, request, *args, **kwargs):
    createdSource = self.createSource(request)
    createdTranslation = Translation.objects.create(
      text = request.data['text'],
      translation = request.data['translation'],
      source = createdSource
    )
    return Response(
      data=TranslationsSerializer(createdTranslation).data,
      status=status.HTTP_201_CREATED
    )

  def createSource(self, request):
    try:
      return Source.objects.create(
        author=request.data['source']['author'],
        url=request.data['source']['url'],
        publisher=request.data['source']['publisher']
      )
    except IntegrityError:
      return Source.objects.get(
        author = request.data['source']['author'],
        url = request.data['source']['url'], 
        publisher = request.data['source']['publisher'])

