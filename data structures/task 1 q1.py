numbers = []
total = 0
count = 0
for i in range(1, 7):
    numbers.append(i)
    total += i
    count += 1


print(numbers[::-1])
print(total)
print(total/count)

