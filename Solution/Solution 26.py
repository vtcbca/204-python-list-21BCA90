'''Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.
   filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]
   Output: filenames = ["program.py", "stdio.py", "sample.py", "a.py", "math.py", "hpp.py"]
   Name : Laxman Sirvi
   Date : 03-04-22'''
f=[]
l=[]
for i in range(5):
    s=input('Enter the filename with extension : ')
    f.append(s)
print('Filename you entered :',f)
r=input('Enter the extension with you want to replace : ')
n=input('Enter new extension : ')
for i in f:
    a=i.replace(r,n)
    l.append(a)
print('Filenames with new extansion :',l)
        
            
