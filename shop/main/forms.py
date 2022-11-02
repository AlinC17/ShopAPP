from django import forms
from .models import ShopItems, Image


class CreateShopItemForm(forms.ModelForm):
    class Meta:
        model = ShopItems
        fields = [
            "item_name",
            "item_price",
            "item_author",
        ]
        labels = {
            "item_name": "Title",
            "item_price": "Price",
            "item_author": "Author",
        }
        widgets = {
            "item_name": forms.TextInput(attrs={'class': 'form-control'}),
            "item_price": forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            "item_author": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
    class Meta:
        model = Image
        fields = ['image',]
        labels = {
            'image': "Image",
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
                'multiple': True,
                'id': 'images-input',
            },),
        }
