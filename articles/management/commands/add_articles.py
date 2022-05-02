from asyncore import read
from django.core.management import BaseCommand
import csv
from articles.models import Article

def get_data(row):
    return {
        "country" : row.get("국가"),
        "date" : row.get("날짜"),
        "category" : row.get("구분"),
        "sector" : row.get("분야"),
        "title_kr" : row.get("제목"),
        "content_kr" : "\n\n".join([row.get(x) for x in ["본문1", "본문2", "본문3"]]),
        "title_local" : row.get("제목_현지공용어"),
        "content_local" : "\n\n".join([row.get(x) for x in ["본문1_현지공용어", "본문2_현지공용어", "본문3_현지공용어"]]),
        "reference" : row.get("출처"),
        "link" : row.get("링크"),
    }
    
def set_article(row):
    article_dict = get_data(row)
    Article.objects.create(**article_dict)   

def set_articles(file):
    reader = csv.DictReader(file)
    for row in reader:
        set_article(row)

def read_from_csv(fpath):
    try:
        with open(fpath, mode="r") as file:
            set_articles(file)

    except UnicodeDecodeError:
        with open(fpath, mode="r", encoding="cp949") as file:
            set_articles(file)


class Command(BaseCommand):
    help = "use can add articles from csv"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('fpath', type=str)

    def handle(self, *arg, **kwarg):
        fpath = kwarg.get("fpath")
        read_from_csv(fpath)
