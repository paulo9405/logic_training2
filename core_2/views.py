from django.shortcuts import render, redirect
from .models import Double
from .forms import DoubleForm
import re


def double_list(request):
    double_data = Double.objects.all()
    return render(request, 'double_lst.html', {'double_data': double_data})


def double_create(request):
    form = DoubleForm(request.POST or None)
    data_name = form.data.get('name')
    data_val = request.POST.get('value')
    data_value = int(data_val or 0)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    data_date_obj = None

    obj = Double.objects.filter(name=data_name, value=data_val)
    if obj.count() > 0:
        data_date_obj = obj[0]

    if data_date_obj is not None:
        return render(request, 'double_exist.html', {'data_name': data_date_obj.name,
                                                     'data_value_obj': data_date_obj.double_value,
                                                     'data_date_obj': data_date_obj.date})

    elif data_value > 1000 or data_value < -1000:
        erro_value = "Please the maximum value is 1000 and the minimum is -1000."
        return render(request, 'double_create.html', {'form': form, 'erro_value': erro_value})

    elif form.is_valid() and (regex.search(data_name) != None):
        erro = "Please Don't use character!"
        return render(request, 'double_create.html', {'form': form, 'erro': erro})

    elif form.is_valid() and (regex.search(data_name) == None):
        form.save()
        return redirect('double_lst')
    return render(request, 'double_create.html', {'form': form})

