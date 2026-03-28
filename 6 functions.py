print("=============================function-to-print================================")
def my_function():
    print("hello dev growth")
my_function()
print("=============================use-of-return================================")
def greeting():
    return "hello"
x= greeting()
print(x)
y=my_function()
print(y) #none aaya kyunki koi return value nhi the
print("=============================pass================================")
def use_of_pass():
    pass #allow you to let fnction block empty
use_of_pass()
print("=============================parameter/argument================================")
def sum(x,y): #x,y are parameter
    return x+y
z=sum(5,6) #5,6 are argument
print(z)
def name(fname):
    print(fname+" "+"world")
name("hello")
print("=============================fahrenhiet to celsius================================")
def conversion(fahrenhiet):
    celsius= (fahrenhiet-32)*(5/9)
    return celsius
x=float(input("enter temp in fahrenhiet :"))
print(f"temp in celsius is {conversion(x)}")
print("=============================positional-argument================================")
def intro(fname,lname,age):
    print(f"first name:{fname}\nlast name:{lname}\nage:{age}")
intro(age=19,lname="gupta",fname="Manthan") #jiss argument ke jo key hai voh ussey he pass krega
print("=============================list================================")
def listt():
    return ["fw","ew","wef"]
fr=listt()
print(fr)
print(len(fr))
print(fr[1])
print("=============================arbitary-argument(*args)================================")
#*args= argument ko tuple ke form mein pass krenge 
def new(*kids):
    print(type(kids))
    print(f"youngest child is {kids}")
new("gr","re","RGe") #args ke use ke vjh se ab jitne ka mnn ho utne argument lo
print("=========================arbitary_keyword-argument(**kwargs)===========================")
# **kwargs =  argument ko dict ke form mein pass krenge 
def func(**kid):
    print(type(kid))
    print("his last name is "+kid["lname"])
    for i,j in kid.items():
        print("key:",i,"\nvalue:",j)
        print("--------------")
func(lname="ddt",fname="fge",age=43)
print("====================================================")
def my__func(title,*args,**kwarg):
    print("title",title)
    print("psitional",args)
    print("keyword",kwarg)
my__func("dev growth","fd","rg","rgrg",age=23,cgpa=10)
print("=======================scope=============================")
a=90 #global variable
def my_func2():
    # a=10 #local variable
    print(a)
print(a)
my_func2()
print("=======================nested-func=============================")
def my_fun3():
    x=3
    def func31():
        print(x)
    func31()
my_fun3()