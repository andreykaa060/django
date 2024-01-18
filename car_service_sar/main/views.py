import re

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ApplicationForm
from .models import Application

# ct89241_db
# EeTXBj7m

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            phone = re.sub(r"[-() ]", '', phone)
            message = form.cleaned_data['message']
            p = Application(name=name, phone=phone, message=message)
            p.save()
            messages.success(request, 'Заявка успешно отправлена')
            return HttpResponseRedirect(request.path)
    else:
        form = ApplicationForm()
    context = {
        'title': 'Ремонт автомобилей в Саратове',
        'address': 'г. Саратов, ул. Черниговская улица, 31',
        'phone': '+7 (987) 820-01-03',
        'work_time_1': 'Пн-Пт: 09.00-20.00',
        'work_time_2': 'Сб: 09.00-18.00',
        'form': form,
        'services': [
            {'name': 'Диагностика автомобиля', 'filename': 'car-repair.svg'},
            {'name': 'Ремонт двигателя', 'filename': 'engine-svgrepo.svg'},
            {'name': 'Ремонт электрики', 'filename': 'energy-svgrepo.svg'},
            {'name': 'Ремонт тормозной системы', 'filename': 'car-wheel.svg'},
            {'name': 'Электронная балансировка и шиномонтаж', 'filename': 'scales-fill.svg'},
            {'name': 'Ремонт рулевого управления', 'filename': 'steering.svg'}
        ]
    }
    return render(request, 'index.html', context)