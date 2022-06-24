from django.shortcuts import render, redirect
from .forms import DoubleForm
from .models import DoubleSave


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

    if form.is_valid():
        form.save()
        return redirect('double_list')

    return render(request, 'double_save.html', {'form': form})


