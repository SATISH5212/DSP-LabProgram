class student:
    a=10
myobj=student()
print(myobj.a)

#class student
class student(object):
    def __init__(self,name,rno):
              self.name=name
              self.rno=rno
    def display(self):
              print(self.name)
              print(self.rno)
s1=student("satish",1)
s1.display()
s2=student("sai",2)
s2.display()
    
