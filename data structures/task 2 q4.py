import random


outletSales = [random.randint(0, 51) for i in range(0, 4)]
print(outletSales)

for quarter in range(0,4):
    total = []
    for outlet in range(0, 50):
        total[quarter] = outletSales[quarter][outlet]

