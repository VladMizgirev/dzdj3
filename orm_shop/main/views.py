from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    list = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'courses-detail'})  # передайте необходимый контекст


def car_details_view(request, car_id):
    try:
        filtered_objects = Car.objects.filter(id=car_id)
        template_name = 'main/details.html'
        return render(request, template_name, {'car-details.html'})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
    # получите авто, если же его нет, выбросьте ошибку 404


def sales_by_car(request, car_id):
    try:
        filtered_car = Car.objects.filter(id=car_id)
        template_name = 'main/sales.html'
        return render(request, template_name, {"{% url 'details' car.id %}"})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
