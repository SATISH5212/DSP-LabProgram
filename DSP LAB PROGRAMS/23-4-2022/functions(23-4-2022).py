def display():
  print("hello world")
display()
#factorial using functions
n=int(input("enter the number"))

def fact(n):     
    f=1      
    for i in range(2, n+1):
        f*= i
    return f
print(fact(n))
