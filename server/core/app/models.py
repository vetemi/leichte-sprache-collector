from django.db import models

class Source(models.Model):
  author = models.CharField(max_length=100)
  url = models.CharField(max_length=512)
  publisher = models.CharField(max_length=100)

  class Meta:
    verbose_name = 'Source'
    verbose_name_plural = 'Sources'
    constraints = [
      models.UniqueConstraint(fields=['author', 'url', 'publisher'], name='uq_source')
    ]

class Translation(models.Model):
  text = models.TextField()
  translation = models.TextField()
  source = models.ForeignKey('Source', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Translation'
    verbose_name_plural = 'Translations'
    constraints = [
      models.UniqueConstraint(fields=['text', 'translation'], name='uq_translation')
    ]
