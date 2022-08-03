import time
start=time.time( )
a=[1,2,3,4]
print(a)
a.insert(4,5)
print(a)
a.pop(0)
print(a)
l=len(a)
print(1)
end=time.time( )
print(f"Runtime of the program is {end - start }")
