# def bes_bastir():
#     print(5)

# def bes_dondur():
#     return 5
# bes_dondur()


"""
def say_hello( name= "user"):
    print("hello " + name)

say_hello("sezai")
"""


# def total(num1,num2):
#     return num1+num2

# Result=total(10,20)
# print(Result)

"""

sehirler = ["ankara", "izmir"]
n=sehirler[:] #slicing, tamamını al
n=sehirler[0:2] #slicing, 0 ila ikinci index arasını al

"""


# def add(a,b,c=0):
#     return sum((a,b,c))

# print(add(10,20))
# print(add(10,20,30))

"""
def add(*params):
    print(params)
    return sum((params))
print(add(10,20,30,50,70,90,100))
"""
"""
def add(*asd):
    print(asd)
    return sum((asd))
print(add(10,20,30,50,70,90,100))
"""

# def display_users(**args):
#     for key, value in args.items():
#         print("{} is {} ".format(key, value))

# display_users(name= "ahmet", age=10, city="ist")
# display_users(name="ali", age=5, city="ank", tel="456789")
# display_users(name="ayşe", age=12, city="izmir", tel="12375", email="asd@asd")


def my_func(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

my_func(10,20,30,40,50,60,70, asd="merhaba", fgh="nbr")


