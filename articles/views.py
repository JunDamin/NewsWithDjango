from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator
from . import models, forms
# Create your views here.


class HomeView(ListView):
    model = models.Article
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "articles"


class ArticleDetail(DetailView):

    """ ArticleDetail Definition """
    model = models.Article


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            title_kr = form.cleaned_data.get("title_kr")
            country = form.cleaned_data.get("country")
            subject_type = form.cleaned_data.get("subject_type")
            sector = form.cleaned_data.get("sector")

            filter_args = {}

            if title_kr:
                filter_args["title_kr__contains"] = title_kr

            if country:
                filter_args["country"] = country

            if subject_type:
                filter_args["category"] = subject_type

            if sector:
                filter_args["sector"] = sector

            qs = models.Article.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            articles = paginator.get_page(page)

            print(articles)

            return render(
                request, "articles/search.html", {"form": form, "articles": articles},
            )

        else:

            form = forms.SearchForm()

            return render(request, "articles/search.html", {"form": form})