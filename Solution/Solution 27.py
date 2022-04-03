'''WAS to create list with 5 string and print only even number character of each string using UDF.
   Name : Laxman Sirvi
   Date : 03-04-22'''
def evench(l):
    for i in l:
        n=[]
        for j in range(len(i)):
            if j%2!=0:
                n.append(i[j])
        print('The even characters in string {} are :'.format(i))
        print(n)
l=[]
for i in range(5):
    s=input('Enter any string : ')
    l.append(s)
evench(l)
        
            
