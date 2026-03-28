print("=============================Set================================")
s1={"Books","Milk","Instant Coffee","Statonary","Chips/kurkure"}
print(s1)
print(type(s1))
s2={2,34,67,8,53,2}  #duplicates not allowed
print(s2)

print("=============================Set-Access (loop)================================")
for i in s1:
    print(i)

print("=============================add================================")
s1.add("Notebook")
print(s1)

print("=============================update================================")
s1.update({"Pen","Pencil"})
print(s1)

print("=============================remove================================")
s3={1,2,3,4,5}
s3.remove(2)   #error if element not present
print(s3)

print("=============================discard================================")
s3.discard(10)  #no error if element not present
print(s3)

print("=============================pop================================")
#random element remove hota hai
s4={10,20,30,40}
x=s4.pop()
print(s4)
print(x)

print("=============================clear================================")
s5={1,2,3}
s5.clear()
print(s5)

print("=============================del================================")
s6={1,2,3}
del s6   #poora set delete

print("=============================union================================")
a={1,2,3}
b={3,4,5}
c=a.union(b)
print(c)

print("=============================intersection================================")
print(a.intersection(b))

print("=============================difference================================")
print(a.difference(b))

print("=============================symmetric_difference================================")
print(a.symmetric_difference(b))

print("=============================copy================================")
d={5,6,7,8}
d2=d.copy()
print(d2)

print("=============================len================================")
print(len(d))

print("=============================using loop-2================================")
d3={11,22,33,44}
for i in d3:
    print(i)

print("=============================question================================")
set1={"apple","banana","cherry","avacado","anda"}
new=set()
for i in set1:
    if i.startswith('a'):
        new.add(i)
print(new)
