'''
1. Write a program that asks for a number N as a user input, and calculates the sum of odd numbers, and the average of even numbers starting from 1 up to and including N
'''

N = int(input("please give a number: "))

odds = []
evens = []

for number in range(1,N+1):
    if number % 2 == 1:
        odds.append(number)
    if number % 2 == 0:
        evens.append(number)

print("sum of odd numbers is: ", sum(odds))
print("average of even numbers is: ", sum(evens)/len(evens))


