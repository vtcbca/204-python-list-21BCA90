''' WAS to implement menu driven program to perform following operation

    1. Print frequency of Character { Rama : R --> 1, a-->2, m-->1 }
    2. Print Only Unique Character { Rama : Ram}
    3. Print Word > n { Print those word from sentence whose length is greater than "n(take input)" }

    Name : Laxman Sirvi
    Date : 02-04-22'''
l=[]
b=[]
a=[]
d=[]
l=input('Enter any string : ')
print("        --:MENU:--")
print("1. Frequency of Characters.")
print("2. Unique Character of string.")
print("3. To print word whose length is greaterthen N.")
n=int(input('Enter your choice : '))
l=l.split()
for i in l:
    for j in i:
        b.append(j)
for i in b:
    c=0
    for j in b:
        if i==j:
            c=c+1
    if i not in a:
        d.append(c)
        a.append(i)
if n==1:
    for i in range(len(d)) :
        print(a[i],'-->',d[i])
elif n==2:
    for i in a:
        print(i,end='')
elif n==3:
    e=int(input('Enter the length of word : '))
    for i in l:
        if len(i)>e:
            print(i)
else:
    print('Enter a valid choise.')
