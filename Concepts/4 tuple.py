print("=============================Tuple================================")
t1=("Books","Milk","Instant Coffee","Statonary","Chips/kurkure")
print(t1)
print(type(t1))
t2=(2,34,67,8,53,2)
print(t2)

print("=============================Tuple-Slicing================================")
print(t1[0:4:2])

print("======================Tuple-combining================================")
t3=t1+t2   #tuples can be concatenated
print(t3)

print("=============================Tuple-Typecast================================")
#string to tuple
txt="SMVDU"
t4=tuple(txt)
print(t4)

t5=tuple([1,2,3,4])
print(t5)

t6=tuple("1,2,3,4,'Manthan'")
print(t6)

print("=============================Add element (workaround)================================")
#tuple is immutable so we create new tuple
t=(1,2,3,4)
m=(5,6,7)
t=t+m
print(t)

print("=============================insert workaround================================")
#convert to list then back to tuple
temp=list(t)
temp.insert(2,55)
t=tuple(temp)
print(t)

print("=============================extend workaround================================")
t1=(1,2,3,4)
m2=(5,6,7)
t1=t1+m2
print(t1)

print("=============================remove workaround================================")
temp=list((1,2,3,4,1))
temp.remove(1)
t2=tuple(temp)
print(t2)

print("=============================pop workaround================================")
temp=list((1,2,3,4,1))
pop=temp.pop()
t3=tuple(temp)
print(t3)
print(pop)

print("=============================del================================")
t4=(1,2,3,4,1)
del t4   #entire tuple delete

print("=============================using loop================================")
t5=(1,2,3,4,1)
for i in t5:
    print(i)

t6=("Books","Milk","Instant Coffee","Statonary","Chips/kurkure")
for i in t6:
    print(i)

print("=============================len===============================")
print(len(t6))

print("=============================using loop-2================================")
for i in range(0,len(t5)):
    print(i,"-->",t5[i])

print("=============================question================================")
tuple1=("apple","banana","cherry","avacado","anda")
new=[]
for i in tuple1:
    if (i.startswith('a')):
        new.append(i)
print(tuple(new))

print("=============================sort workaround================================")
#tuples cannot be sorted directly
temp=list((1,5,6,3,2,6,8,5,4))
temp.sort()
t_sorted=tuple(temp)
print(t_sorted)

a=("apple","banana","cherry","avacado","anda")
temp=list(a)
temp.sort(key=len)
a_sorted=tuple(temp)
print(a_sorted)

print("=============================copy================================")
t=(1,5,6,3,2,6,8,5,4)
t2=tuple(t)   #copy via constructor
print(t2)

print("=============================count================================")
print(t.count(1))
