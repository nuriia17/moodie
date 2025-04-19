myfamily = ['father', 'mother', 'brother', 'sister', 'brother']
print(myfamily)
print(type(myfamily))
print(myfamily[3])
myfamily.append('Nuriia') #it will not work because of the bracket
myfamily.pop(2)
print(myfamily)

laptop = {"brand":"dell", "model":"alienware", "year":"2010"}
print(laptop["brand"])
laptop["home"]=True
print(laptop)
laptop["year"] = 2019
print(laptop)

name= input("Write your name")
age = input("Write your age")
country = input("Where are you from?")
user_known = input("Do you know  me?")

user_info = {
    "name":name,
    "age":age,
    "country":country,
    "user_known":user_known
}
print("\nUser information:")
print(f"Name: {user_info['name']}")
print(f"Age: {user_info['age']}")
print(f"Country: {user_info['country']}")
print(f"User_known: {user_info['user_known']}")