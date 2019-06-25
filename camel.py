import math
totalBanana = 3000
camelCapacity = 1000
bananaPerKilometer = 1
totalBananaLeft = 0
totalDistance = 1000


def Calculate(totalBanana, camelCapacity, bananaPerKilometer, no0fDonkeys, totalDistance):
  miles = 0
  t = totalBanana // camelCapacity
  for i in range(1, t+1):
      miles = miles + camelCapacity/((2*i) - 1)
  print(miles)
  mile = miles // bananaPerKilometer
  print(mile)
  return mile - totalDistance


bananaleft = Calculate(totalBanana, camelCapacity, 1, 1, totalDistance)
print(math.floor(bananaleft))
