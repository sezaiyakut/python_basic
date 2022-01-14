# name='Sezai Yakut'
# for letter in name:
#         if letter == "i":
#             break
#         print(letter)

# name='Sezai Yakut'
# for letter in name:
#         if letter == "i":
#             continue
#         print(letter)

result=0
x=0
while x<100:
    x+=1
    
    if x%2==0:
        continue
    result=result+x
print(result)