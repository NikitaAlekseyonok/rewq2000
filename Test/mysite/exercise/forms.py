from django import forms


class InputForm(forms.Form):
    name0 = forms.CharField(label='field_name', max_length=50)

