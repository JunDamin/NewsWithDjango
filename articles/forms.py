from django import forms
from . import models


class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = (
            "date",
            "title_kr",
            "country",
            "category",
            "sector",
        )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False