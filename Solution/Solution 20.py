''' WAS to create UDF which check string is palindrom or not.
    Name : Laxman Sirvi
    Date : 02-04-22'''
def palin():
    s=input('Enter any string : ')
    r= "".join(reversed(s))
    if s==r:
        print("{} is palindrom".format(s))
    else :
        print ("{} is not palindrom.".format(s))
palin()
