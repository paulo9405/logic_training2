from django.shortcuts import render, redirect


def double3(request):
    data = 0
    if request.method == 'POST':
        data = request.POST.get('valueuser')
        double = int(data) * 2

    return render(request, 'double2.html', {'double': double})
