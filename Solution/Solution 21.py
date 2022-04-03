''' WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.
    strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.
    Name : Laxman Sirvi
    Date : 02-04-22'''
def strSymmetric(s):
    b=s
    a=len(s)//2
    if s[:a]==s[a:]:
        print(b,' is a symmetric string.')
    else:
        print(b,' is not a symmetric string.') 
def inpu():
    s=input('Enter any string : ')
    strSymmetric(s)
inpu()
