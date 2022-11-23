from django import forms


class ColorPickerForm(forms.Form):
    red_input = forms.IntegerField(
        min_value=0,
        max_value=255,
        required=True,
        label='Red Value'
    )
    green_input = forms.IntegerField(
        min_value=0,
        max_value=255,
        required=True,
        label='Green Value'
    )
    blue_input = forms.IntegerField(
        min_value=0,
        max_value=255,
        required=True,
        label='Blue Value'
    )
