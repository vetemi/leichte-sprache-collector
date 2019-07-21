
from django.urls import path
from .views import ListCreateTranslationView

urlpatterns = [
  path('translations/', ListCreateTranslationView.as_view(), name="translations-list-create")
]
