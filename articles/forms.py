from django import forms
from . import models


class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = (
            "title_kr",
            "country",
            "category",
            "sector",
        )
        
        widgets = {
            "title_kr": forms.TextInput(attrs={"placeholder": "제목"}),
            "country": forms.TextInput(attrs={"placeholder": "국가"}),
            "category": forms.TextInput(attrs={"placeholder": "구분: KOICA, 수원국, 공여국, 국제기구"}),
            "sector": forms.TextInput(attrs={"placeholder": "분야"}),
        }

    start_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '범위시작 YYYY-MM-DD', 'required': False}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '범위종료 YYYY-MM-DD', 'required': False}))


    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False


class FileForm(forms.Form):
    csv = forms.FileField(widget=forms.FileInput(attrs={"placeholder": "upload CSV file"}))