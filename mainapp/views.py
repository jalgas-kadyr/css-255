from django.shortcuts import render
from django.http import HttpResponse
from .models import Object


def index(request):
    return render(request, 'index.html')


def katalog(request, katalog):
    objects = Object.objects.filter(type=katalog)
    return render(request, 'foods.html', {'objects': objects})


def add(request, type):
    objects = Object.objects.filter(type=type)
    response = render(request, 'foods.html', {'objects': objects})
    try:
        data = request.COOKIES['basket']
        codes = [int(word) for word in data.split() if word.isdigit()]
        add = True
        for i in codes:
            if i == request.POST['code']:
                add = False
        if add:
            data = data + ' '
            code = request.POST['code']
            data = data + code
            response.set_cookie('basket', str(data))
        else:
            pass
    except Exception as error:
        data = request.POST['code']
        print(data)
        response.set_cookie('basket', data)
    return response


def basket(request):
    data = request.COOKIES['basket']
    codes = [int(word) for word in data.split() if word.isdigit()]

    objects = []
    for i in codes:
        objects.append(Object.objects.get(code=str(i)))
    return render(request, 'basket.html', {'objects': objects})


def sbross(request):
    response = render(request, 'basket.html', {'objects': []})
    response.set_cookie('basket', '')
    return response
