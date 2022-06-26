from django.shortcuts import render, redirect
from .forms import DoubleForm
from .models import DoubleSave
import re



def double3(request):
    data = 0
    double = 0
    if request.method == 'POST':
        data = request.POST.get('valueuser')
        double = int(data) * 2

    return render(request, 'double2.html', {'double': double})


def double_list(request):
    double_data = DoubleSave.objects.all()
    return render(request, 'double_list.html', {'double_data': double_data})


def double_save(request):
    form = DoubleForm(request.POST or None)
    data_name = form.data.get('name')
    data_val = request.POST.get('value')
    data_value = int(data_val or 0)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


    if data_value > 1000 or data_value < -1000:
        erro_value = "Please the maximum value is 1000 and the minimum is -1000."
        return render(request, 'double_save.html', {'form': form, 'erro_value': erro_value})

    elif form.is_valid() and (regex.search(data_name) != None):
        erro = "Please Don't use character!"
        return render(request, 'double_save.html', {'form': form, 'erro': erro})

    elif form.is_valid() and (regex.search(data_name) == None) :
        form.save()
        return redirect('double_list')

    return render(request, 'double_save.html', {'form': form})




# def double_save(request):
#     form = DoubleForm(request.POST or None)
#     data_name = form.data.get('name')
#     data_value = form.data.get('value')
#     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#
#     if form.is_valid() and (regex.search(data_name) == None) :
#         form.save()
#         return redirect('double_list')

#     elif form.is_valid() and (regex.search(data_name) != None) :
#         erro = "Please Don't use character!"
#         return render(request, 'double_save.html', {'form': form, 'erro': erro})
#
#     return render(request, 'double_save.html', {'form': form})


# def double_save(request):
#     form = DoubleForm(request.POST or None)
#     data = form.data.get('name')
#     # regex = ('[@_!#$%^&*()<>?/\|}{~:]')
#     regex = ['@', '_', '!', '#', '$',
#                        '%', '^', '&', '*', '()',
#                        '<', '>', '?', '/\|', '}',
#                        '{', '~', ':']
#     for i in regex:
#         if form.is_valid() and i not in data:
#             form.save()
#             return redirect('double_list')
#
#         elif form.is_valid() and i in data:
#             erro = "Please Don't use character!"
#             return render(request, 'double_save.html', {'form': form, 'erro': erro})
#
#     return render(request, 'double_save.html', {'form': form})