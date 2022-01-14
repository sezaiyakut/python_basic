name = "Sezai"
surname = "Yakut"
age = 26
greeting = "Merhaba, ben" + " " + name + " " + surname + "\n" + str(age) + " " + "yaşındayım"
#print (greeting)
length = len(greeting)
# print(greeting[3])
# print(greeting[6])
#print(len(greeting))

#son harfi çağırmak için;
#print(greeting[length-1])
#print(greeting[-1])

#Belli aralıktaki harfleri çağırmak için;

print(greeting[2:5])
print(greeting[:5])
print(greeting[:20])
print(greeting[5:])
print(greeting[2:40:2])
