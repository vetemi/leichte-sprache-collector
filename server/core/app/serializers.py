from rest_framework import serializers
from .models import Translation

class TranslationsSerializer(serializers.ModelSerializer):
  class Meta:
      model = Translation
      fields = ('text', 'translation', 'source')
