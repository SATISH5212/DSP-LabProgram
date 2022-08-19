import numpy as np

a=np.arange(15).reshape(3,5)
print(a)
b=np.array([3,4.5,8])
print(b)
print(type(a))
print(type(b))
print(a.itemsize)
print(b.itemsize)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(b.dtype)
c=np.linspace(0, 2, 9)   
print(c)
d=np.arange(10000)
print(d)

