"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

pal = 1 11 22 33 111 121 222 212 232


"""

s = ""

def isPanlindrome(s):
    if s[0] == s[-1] :
        return print("True")
    elif s[0] == s[-1] and s[1] == s[-2] :
        return print("True")
    else:
        return print("False")



print(isPanlindrome("121"))

def productPal(num1, num2):
    for num1 in range(999):

