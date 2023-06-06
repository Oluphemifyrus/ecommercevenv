from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 101)]

# products = Product.objects.all()

# PRODUCT_QUANTITY_CHOICES = []
# for product in products:
#     choice = [(i, str(i)) for i in range(1, product.availableUnit + 1)]

#     PRODUCT_QUANTITY_CHOICES.extend(choice)


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)