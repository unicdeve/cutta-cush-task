from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .max_banana import max_banana

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
  max_banana_sales = 0
  if request.method == 'POST':
    x_bananas = request.POST.get('x_bananas')
    y_distance = request.POST.get('y_distance')
    z_camels = request.POST.get('z_camels')

    max_banana_sales = max_banana(x_bananas=x_bananas, y_distance=y_distance, z_camels=1, camels_capacity=1000, eats_per_km=1)

    data = [{ 'banana_left_for_sale': max_banana_sales, 'z_camels': z_camels, 'x_bananas': x_bananas, 'y_distance': y_distance }]
    return JsonResponse(data, safe = False)

  return render(request, 'camel/index.html')