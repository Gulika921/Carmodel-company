from django import forms
from car.models import Car, CarModel, Company


class CarForm(forms.ModelForm):

    # name = forms.CharField(max_length=100)
    # vin_number = forms.CharField(max_length=100)

    class Meta:
        model = Car
        fields = "__all__"


class CarModelForm(forms.ModelForm):

    class Meta:
        model = CarModel
        fields = "__all__"


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = "__all__"
