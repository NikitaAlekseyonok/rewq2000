from django.shortcuts import render, redirect
from .models import *
from .forms import *
import json


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            name_input = form.cleaned_data['name0']
            data = json.dumps(name_input, ensure_ascii=False)
            InputModel.objects.create(data=data, input_field='name0')

            for count in range(1, len(request.POST) - 1):
                query = 'name' + str(count)
                input_value = request.POST[query]

                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    InputModel.objects.create(data=data, input_field=field)

                count += 1
        return redirect('/done/')

    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})


def done(request):
    query = InputModel.objects.all().values('id', 'input_field', 'data')
    json_list = list(query)
    return render(request, 'done.html', {'json_list': json_list})
