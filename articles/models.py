from django.db import models
from core import models as core_models
# Create your models here.


# ,국가,날짜,구분,분야,제목,본문1,본문2,본문3,제목_현지공용어,본문1_현지공용어,본문2_현지공용어,본문3_현지공용어,출처,링크

class Article(core_models.TimeStampedModel):
    """
    content_kr: merge 본문1,본문2,본문3
    content_local: moerge 
    """
    country = models.CharField(max_length=80)
    date = models.DateField()
    category = models.CharField(max_length=80)
    sector = models.CharField(max_length=80)
    title_kr = models.CharField(max_length=255)
    content_kr = models.TextField()
    title_local = models.CharField(max_length=255)
    content_local = models.TextField()
    reference = models.CharField(max_length=255)
    link = models.TextField()
