import pygame 
numbers = []
def CalcSumNumbers(numbers):
    if numbers == []:
        return 0
    else:
        sum=CalcSumNumbers(numbers[1:])
        sum = sum + numbers[i]
        return sum 

a = input(int())
for i in range(a):
    a = int(input())  # считываем очередной элемент
    a.append(a)
    
a.append(numbers)
sum = CalcSumNumbers(numbers)
print(sum)