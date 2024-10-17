number = input("enter a number")
palindrome = False
list1 = []
list2 = []

for i in range(0, len(number)):
    list1.append(number[i])

for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])

for i in range(0, len(list1)):
    if list1[i] != list2[i]:
        palindrome = False
        break
    elif list1[i] == list2[i]:
        palindrome = True
    
if palindrome == True:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")


