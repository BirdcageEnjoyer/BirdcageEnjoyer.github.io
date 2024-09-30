quarter1 = 0
quarter2 = 0
quarter3 = 0
quarter4 = 0

outlet1Sales = [10, 12, 15, 10]
outlet2Sales = [5, 8, 3, 6]
outlet3Sales = [10, 12, 15, 10]
salesCombined = []
salesCombined.extend([outlet1Sales, outlet2Sales, outlet3Sales])
# returns [[10, 12, 15, 10], [5, 8, 3, 6], [10, 12, 15, 10]]

for outlet in salesCombined:
    quarter1 += outlet[0]
    quarter2 += outlet[1]
    quarter3 += outlet[2]
    quarter4 += outlet[3]

print("Total for quarter 1", quarter1)
print("Total for quarter 2", quarter2)
print("Total for quarter 3", quarter3)
print("Total for quarter 4", quarter4)
