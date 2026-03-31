print("=============================concatination================================")
s1="Manthan"
s2="gupta"
s3=s1+" "+s2  #it is order specific
print(s3)

print("=============================List================================")
l1=["Books","Milk","Instant Coffee","Statonary","Chips/kurkure"]
print(l1)
print(type(l1))
l2=[2,34,67,8,53,2]
print(l2)

print("=============================List-Slicing================================")

print(l1[0:4:2])

print("======================List-combining or append method===================")
l3=l1+l2
print(l3)
l4=l1.append(l2)
print(l4)

print("=============================List-Typecast================================")
#string to list
txt="SMVDU"
s3=list(txt)
print(s3)

s4=list([1,2,3,4])
print(s4)
s5=list("1,2,3,4,'Manthan'")
print(s5)

print("=============================Append 2================================")
l=[1,2,3,4]
m=[5,6,7]
l.append(m) #work only in same data type
print(l)

print("=============================insert================================")
l.insert(2,55) #(index,element)
print(l)

print("=============================extend================================")
l1=[1,2,3,4]
m2=[5,6,7]
l1.extend(m2) #dfferent data type bhi add ho aate hai jaise list+tuple
print(l1)
m1=(5,6,7)
l1.extend(m1)
print(l1)
print("=============================remove================================")
#first occurence ko remove kr dega 
l2=[1,2,3,4,1]
l2.remove(1)
print(l2)
print("=============================pop================================")
#it returns it itself and by default it remove last one 
l3=[1,2,3,4,1]
pop= l3.pop()
print(l3)
print(pop)
print("=============================del================================")
#by default puri list delete kr deta hai 
l4=[1,2,3,4,1]
del l4[2]
print(l4)
print("=============================using loop================================")
l5=[1,2,3,4,1]
for i in l5:
    print(i)
l6=["Books","Milk","Instant Coffee","Statonary","Chips/kurkure"]
for i in l6:
    print(i)
print("=============================len===============================")
print(len(l6))
print("=============================using loop-2================================")

for i in range(0,len(l5)):
    print(i,"-->",l5[i])

print("=============================question================================")
list1=["apple","banana","cherry","avacado","anda"]
new=[]
for i in list1:
    if (i.startswith('a')): #i[0]=='a'
        new.append(i)
print(new)

print("=============================sort================================")
l=[1,5,6,3,2,6,8,5,4]
l.sort()
print(l)
a=["apple","banana","cherry","avacado","anda"]
a.sort(key=len)
print(a)

print("=============================copy================================")
l=[1,5,6,3,2,6,8,5,4]
l2=l.copy()
print(l2)
l3=l[:]
print(l3)
print("=============================count================================")
print(l.count(1))