school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [4, 7, 1, 3]
schoolNumber = 0

while schoolNumber != -1:
    schoolNumber = int(input("enter school number 1 to 4, -1 to end"))
    if schoolNumber < 0 or schoolNumber > 4:
        print("invalid input")
        continue
    newResult = int(input("enter the new result"))
    if newResult < 0:
        print("invalid input")
        continue

    if 4 > schoolNumber > 0:
        medal[schoolNumber-1] = newResult

for i in range(0, 4):  
    print("school number", i + 1, "school name", school[i], "medals:", medal[i])

    