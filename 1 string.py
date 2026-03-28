txt="Hello, world!"
print(txt)
print(type(txt))
txt2='Hello, world!'
print(txt2)

#string array e form men store hota hai 

print("===========================Use of triple quotes==================================")

txt3='''Name = Manthan
Course = Btech(Mathematics and Computing)
Entry Number = 25bcm028'''
print(txt3)

print("=============================================================")

txt4='''"My name is "Manthan Gupta" "'''
print(txt4)
print("-------------------------------------------------------------")
txt5="My name is "'Manthan Gupta'" "
print(txt5)
print("-------------------------------------------------------------")
txt6="My name is "'''Manthan Gupta'''" "
print(txt6)
print("-------------------------------------------------------------")
txt7="My name is \"Manthan Gupta\" "
print(txt7)


print("========================String using loops=====================================")

txt8="SMVDU"
for x in txt8:
    print(x)


print("==========================Len Function===================================")


print(len(txt))
print(len(txt2))
print(len(txt3))
print(len(txt4))
print(len(txt5))
print(len(txt6))
print(len(txt7))
print(len(txt8))


print("============================in function=================================")


txt9="Jai Mata Di"
print("Di" in txt9)
print("Di" not in txt9)


print("=========================using if and in simultaneously====================================")


txt10="Jai Mata Di"
if("Di" in txt10):
    print("yes it is present")


print("==========================String indexng===================================")


txt11="Indexing"
print(txt11[0])
print(txt11[-5]) #org index = len(txt11)-5 ==> 3
print(txt11[3])


print("=============================String slicing================================")


txt12="String slicing"
print(txt12[0:]) #end tk jayega
print(txt12[:10]) #start se start hoga
print(txt12[3:10])
print(txt12[5:len(txt12)])
print(txt12[:])
print(txt12[-5:-2])
print(txt12[-2:-5]) #nhi chlega bs space print hoga
print(txt12[::2]) #shuru se end tk 2 ke gap mein 

print("=============================lower/upper function================================")


txt13="SMVDU"
print(txt13.lower())
print(txt13.islower())
print(txt13.isupper())
txt14="smvdu"
print(txt14.upper())


print("=============================strip function================================")


#to remove something from coreners by default space
txt15="         Manthan         "
print(txt15.strip())


print("=============================replace function================================")


txt16="we are studying at SMVDU"
print(txt16)
print(txt16.replace("SMVDU","NIT Katra"))


print("=============================split function================================")


txt17="we are studying at SMVDU"
print(txt17.split(" "))


print("=============================capitalize function================================")


txt18="we are studying at SMVDU"
print(txt18.capitalize())


print("=============================casefold function================================")



#almost same as lower


print("=============================centre function================================")


txt19="SMVDU"
print(txt19.center(20,"+")) #string ke total length 20 ke ho jayegi


#baaki function ke liye W3 school mein jao