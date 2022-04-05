'''Create a list using UDF by appending points of cricket team after compliting their qualifing round of 5 teams. Print the runner's team point.
   Note: There is a chance that 2 or more teams gets a same point. Also there is no possibility that each team has same point.
   For example :
   case 1: point=[10,8,14,6,12]
   Output : 12
   case 2: Point=[10,8,14,14,12]
   output:  12
   Name : Laxman Sirvi
   Date : 04-04-22'''
def score():
    l=[]
    l1=[]
    for i in range(5):
        a=int(input('Enter the score point of team 1 : '))
        l.append(a)
    print(l[-1])
    for i in range(5):
        b=int(input('Enter the score point of team 2 : '))
        l1.append(b)
    print(l1[-1])
score()
    
    
