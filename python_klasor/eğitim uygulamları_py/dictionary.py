#41=>Kocaeli 34 => Istanbul

# sehirler = ["Kocaeli","Istanbul"]
# plakalar = [41,34]

# print(plakalar[sehirler.index("Istanbul")])

# plakalar = { "Kocaeli" : 41, "Istanbul" : 34}
# print(plakalar["Kocaeli"])

# plakalar["Ankara"] = 6
# print(plakalar)
"""
users= {
    "Sezai Yakut" : 
    {"age" : 26,
    "Job": "Engineer",
    "E-mail" : "sezai.yakutt@gmail.com"}
    ,
    "Ahmet Yakut" : 
    {"age" : 64,
    "Job" : "Retired",
    "E-mail": "None"}
}
print(users["Sezai Yakut"])
print(users["Ahmet Yakut"])

print(users["Sezai Yakut"]["Job"])
"""

# students= {100:
# {
#     "Name":"Sezai",
#     "Surname":"Yakut",
#     "Phone Number":"05342468445"
# }}
# print(students[100]["Soyad"])

students={}


number=input("Student Number:")
name=input("Name:")
surname=input("Surname:")
phone=input("Phone Number")

students.update({
    number: {
        "Name":name,
        "Surname":surname,
        "Phone Number":phone

    }
})

number=input("Student Number:")
name=input("Name:")
surname=input("Surname:")
phone=input("Phone Number")

students.update({
    number: {
        "Name":name,
        "Surname":surname,
        "Phone Number":phone
        
    }
})

number=input("Student Number:")
name=input("Name:")
surname=input("Surname:")
phone=input("Phone Number")

students.update({
    number: {
        "Name":name,
        "Surname":surname,
        "Phone Number":phone
        
    }
})

students[number] = {
    "Name":name,
    "Surname":surname,
    "Phone Number":phone

}

students.update({
    number: {"
    "
        "Name":name,
        "Surname":surname,
        "Phone Number":phone
        
    }
})

print(students)