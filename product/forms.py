from django import forms

from product.models import Product, Version
from product.forms_mixins import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        #        fields = ('name', 'description', 'price', )
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        description = self.cleaned_data['description']

        for word in forbidden_words:
            print(word)
            print(description)
            if word in description:
                raise forms.ValidationError(f'Слово {word} ай-ай-ай на сайте')

        return description

class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'title', 'release_date')
