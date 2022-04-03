'''WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().
   Name : Laxman Sirvi
   Date : 03-04-22'''
def evenOdd(l):
    e=[]
    o=[]
    c=0
    d=0
    for i in l:
        if i%2==0:
            c+=1
            e.append(i)
        else :
            d+=1
            o.append(i)
    print('There are total {} even No. in list : '.format(c),end='')
    for i in e:
        print(i,end=' ')
    print('')
    print('There are total {} odd No. in list : '.format(d),end='')
    for i in o:
        print(i,end=' ')
def createList():
    l=[]
    for i in range(5):
        n=int(input('Enter any integer value : '))
        l.append(n)
    evenOdd(l)
createList()
