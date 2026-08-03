from django.shortcuts import get_object_or_404, render

from .forms import EbookSearchForm
from .models import Ebook

# Create your views here.

def ebook(request, id):
    ebook = get_object_or_404(Ebook, id=id)
    return render(request, 'ebook.html', {'ebook': ebook})

def ebook_search(request):
    form = EbookSearchForm(request.GET)
    ebooks = Ebook.objects.all()
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            ebooks = ebooks.filter(title__icontains=query)
    return render(request, 'ebook_search.html', {'form': form, 'ebooks': ebooks})