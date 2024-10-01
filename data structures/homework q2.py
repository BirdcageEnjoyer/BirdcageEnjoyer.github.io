group1 = []
group2 = []
pupils = [] 
for i in range(0, 20):
    nameOfPupil = input("enter pupil name")
    pupils.append(nameOfPupil)
#endfor

for x in range(0, 20):
    if x % 2 == 0:
        group1.append(pupils[x])
    else:
        group2.append(pupils[x])
    #endif
#endfor

print("group 1 consists of", ', '.join(group1))
print("group 2 consists of", ', '.join(group2))

