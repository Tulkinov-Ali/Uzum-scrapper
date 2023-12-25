import time

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils import process_product


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def process_product_view(request):
    error_message = None

    if request.method == 'POST':
        product_url = request.POST.get('product_url', '')
        delay_time = int(request.POST.get('delay_time', 0))

        if delay_time > 0:
            time.sleep(delay_time)

        result, error_message = process_product(product_url)

        if result is not None:
            return render(request, 'index.html', {'result': result})

    return render(request, 'index.html', {'error_message': error_message})
