from django import forms


class EbookSearchForm(forms.Form):
    query = forms.CharField(
        label="Pesquisar",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Digite o nome do livro...", 'class': 'form-control'}),
    )
