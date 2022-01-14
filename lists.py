# message="Hello There. My name is Sezai YAKUT".split()
# print(message)

# list1=["one","two","three"]
# list2=["four","five","six"]
# numbers=list1+list2
# print(numbers)
# print(len(numbers))

from types import DynamicClassAttribute


carlist=["Bmw","Mercedes","Opel","Mazda"]
# print(len(carlist))
# print(carlist[0:4:3])
# carlist[-1]="Toyota"
# print(carlist)
# result="Mercedes" in carlist
# carlist[-2:] = ["Toyota","Renault"]
# result=carlist
# print(result)
carlist=carlist+["Audi","Nissan"]
print(carlist)
del carlist[-1]
print(carlist)
result=carlist[::-1]
print(result)

studentA= ["Sezai", "Yakut", 1995, [80,90,100]]
print(studentA[3][2])
result=f"{studentA[0]} Yakut {2021-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+ studentA[3][1]+studentA[3][2])/3}'dır."
print(result)