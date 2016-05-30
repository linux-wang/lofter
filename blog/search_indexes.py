import datetime
from haystack import indexes
from models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(use_template=True)
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
