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
            category = form.cleaned_data.get("category")
            sector = form.cleaned_data.get("sector")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            

            filter_args = {}

            if title_kr:
                filter_args["title_kr__contains"] = title_kr

            if country:
                filter_args["country"] = country

            if category:
                filter_args["category"] = category

            if sector:
                filter_args["sector"] = sector

            if start_date:
                filter_args["date__gte"] = start_date

            if end_date:
                filter_args["date__lte"] = end_date

            qs = models.Article.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            articles = paginator.get_page(page)

            return render(
                request, "articles/search.html", {"form": form, "articles": articles},
            )

        else:

            form = forms.SearchForm()

            return render(request, "articles/search.html", {"form": form})