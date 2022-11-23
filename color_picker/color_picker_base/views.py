from django.shortcuts import render
from django.views import View
from color_picker_base.forms import ColorPickerForm

# Create your views here.


class ColorPickerView(View):
    def get(self, request):
        # Show the user the form and color
        form = ColorPickerForm()

        default_red = 255
        default_green = 255
        default_blue = 255

        html_data = {
            'form': form,
            'red': default_red,
            'green': default_green,
            'blue': default_blue
        }

        return render(request=request, template_name='home.html', context=html_data)

    def post(self, request):
        color_form = ColorPickerForm(request.POST)

        red_value = int(request.POST['red_input'])
        green_value = int(request.POST['green_input'])
        blue_value = int(request.POST['blue_input'])

        html_data = {
            'form': color_form,
            'red': red_value,
            'green': green_value,
            'blue': blue_value
        }

        return render(
            request=request,
            template_name='home.html',
            context=html_data
        )
