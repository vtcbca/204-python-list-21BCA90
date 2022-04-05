'''WAS To create list using UDF with duplicate number and print only unique value from it using UDF.
   Name : Laxman Sirvi
   Date : 03-04-22'''
def unique(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    print('These are the unique value you enterd :',a)
def duplicate():
    l=[]
    for i in range(5):
        n=int(input('Enter any integer value : '))
        l.append(n)
    unique(l)
duplicate()
            
