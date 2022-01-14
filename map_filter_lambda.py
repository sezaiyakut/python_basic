# def square(num):return num **2


# numbers=[1,3,5,9]

# result= list(map(square, numbers))

# print(result)

# for i in map(square,numbers):
#     print(i)



"""
##  --  alakasız alıştırma   --   ##


def square(num, num2):
     print(num*2, num2*2)

qwe=square(2,4)

kutu=[]
def asd(*num):
    
    for n in num:
            a=n*2
            kutu.append(a)
    print(kutu)
            

asd(3,6,5,10)

"""



# square= lambda num: num ** 2

# numbers=[1,3,5,9]

# result=square(3)

# print(result)

"""
numbers=[1,3,5,9]
result= list(map(lambda num:num**2,numbers))

print(result)

"""

# numbers=[1,3,5,9,4,10]
# def check_even(num): return num%2==0
# result= list(filter(check_even, numbers))
# print(result)

from types import resolve_bases


numbers=[1,3,5,9,4,10]
Result=list((filter(lambda num: num%2==0, numbers)))
print(Result)