from django.urls import path
from color_picker_base.views import ColorPickerView

urlpatterns = [
    path('', ColorPickerView.as_view(), name='paint')
]
