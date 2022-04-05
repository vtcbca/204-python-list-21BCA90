''' WAS to create UDF which create 2 list Student and Address which contain student name and respected address of student.
    Create new UDF which print student name with appropiate student address. 
    Name : Laxman Sirvi
    Date : 02-04-22'''
def prin(l1,l2):
    for i in range(3):
        print('{} live in {}'.format(l1[i],l2[i]))
def inpu():
    l1=[]
    l2=[]
    for i in range(3):
        l=input("Enter the name of student's : ")
        l1.append(l)
        l=input("Enter the Address of student's : ")
        l2.append(l)
    prin(l1,l2)
inpu()
