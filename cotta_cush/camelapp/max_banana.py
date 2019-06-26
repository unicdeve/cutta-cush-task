import math

x_bananas = 3000
camels_capacity = 1000
eats_per_km = 1
z_camels = 1
y_distance = 1000

eats_per_km = 1

def max_banana(x_bananas, y_distance, z_camels=1 , camels_capacity=1000, eats_per_km=1):
  miles = 0
  t = int(x_bananas) // int(camels_capacity)
  for i in range(1, t+1):
      miles = miles + camels_capacity/((2*i) - 1)
  mile = miles // eats_per_km
  return int(mile) - int(y_distance)

max_banana_sales = math.floor(max_banana(x_bananas, y_distance, z_camels=1, camels_capacity=1000, eats_per_km=1))
# print(max_banana_sales)