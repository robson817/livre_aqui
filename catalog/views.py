from django.core.paginator import Paginator
from django.shortcuts import render

from ebook.models import Ebook
from movie.models import Movie


def home(request):
    # 1. Busca e paginação dos filmes
    movie_page = request.GET.get("movie_page", 1)
    movies_ordered = Movie.objects.all().order_by("-created_at")
    movie_paginator = Paginator(movies_ordered, 4).get_page(movie_page)

    # 2. Busca e paginação dos e-books (só executa no carregamento normal da Home)
    ebook_page = request.GET.get("ebook_page", 1)
    ebook_ordered = Ebook.objects.all().order_by("-created_at")
    ebook_paginator = Paginator(ebook_ordered, 4).get_page(ebook_page)

    # 3. Se a requisição veio do HTMX (clique na seta dos livros)
    if request.headers.get("HX-Request"):
        if 'ebook_page' in request.GET:
            return render(request, "partials/ebook_list.html", {"ebooks": ebook_paginator})
        return render(request, "partials/movie_list.html", {"movies": movie_paginator})

    # 4. Retorno do carregamento inicial da página inteira
    return render(
        request,
        "home.html",
        {
            "movies": movie_paginator,
            "ebooks": ebook_paginator,
        },
    )


def about(request):
    return render(request, "about.html")
