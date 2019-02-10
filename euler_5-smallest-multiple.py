"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

num = 2520

def divideby(numbers):
    for div in range(1,11):
        if not(numbers %div == 0):
            return False
    return True


for numbers in range(1,5000):
    if divideby(numbers) == True:
        print("dividable numbers: ", numbers)



#
#
#
# for numtwo in range(1,100):
#     for x in range(1,20):
#         if numtwo % x in range(1,20) == 0:
#             print("liczba podzielna przez 1-20 to: ",numtwo)
#         else:
#