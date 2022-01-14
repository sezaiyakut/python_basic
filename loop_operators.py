#range

# for a in range(100):
#     print(a)

# for item in range(5,50,5):
#     print(item)

# print(list(range(3,30,3)))




"""numerate"""

"""
greeting='Hello'
for l in greeting:
    print(l)
"""

# index=0
# greeting='Hello'
# for l in greeting:
#     print(f"index: {index}, Letter: {l}")
#     index+=1


"""
index=0
greeting='Hello'
for item in enumerate(greeting):
    print(item)
"""

# index=0
# greeting='Hello'
# for index, letter in enumerate(greeting):
#     print(f"index: {index}, letter: {letter} ")


"""
zip


list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))
for a,b,c in zip(list1,list2, list3):
    print(a)

"""



# numbers= []
# for x in range (10):
#     numbers.append(x)
# print(numbers)

"""
numbers=[x for x in range(10)]
print(numbers)
"""


# numbers=[x**2 for x in range(10)]
# print(numbers)

"""
numbers=[x*x for x in range(10) if x%3==0]
print(numbers)
"""

# greeting="Hello"
# mylist=[]
# for l in greeting:
#     mylist.append(l)
# print(mylist)


"""
greeting="Hello"
mylist=[l for l in greeting]
print(mylist)
"""

# years=[1995, 1998, 1999, 2005, 1987]
# ages=[2021-year for year in years]
# print(ages)

"""
results=[ x if x%2==0 else "TEK" for x in range(1,10) ]
print(results)
"""

# result=[]
# for k in range(3):
#     for l in range(3):
#         result.append((k,l))
# print(result)  ##  = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
