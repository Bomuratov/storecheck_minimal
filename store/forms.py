from django import forms

from store.models import Visit, Territory, Trade, Sku


class VisitForm(forms.ModelForm):
    trade = forms.Select()
    territory = forms.Select()
    sku = forms.ChoiceField()
    comment=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Comment')

    class Meta:
        model = Visit
        fields = ['trade', 'territory', 'sku', 'comment']


class TerritoryForm(forms.ModelForm):
    territory_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Name of Territory')

    class Meta:
        model = Territory
        fields = ['territory_name']


class TradeForm(forms.ModelForm):
    trade_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Name of Trade')

    class Meta:
        model = Trade
        fields = ['trade_name']


class SkuForm(forms.ModelForm):
    img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Image', required=False)
    sku_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Name of SKU')

    class Meta:
        model = Sku
        fields = ['img', 'sku_name']