#  Print First "Hello World"
print("Hello World")

#  *** Data Types ***

# String
my_name:str = "Humaira Osama"
print(type(my_name),"My name is", my_name)

# Integers
my_age:int = 32
print(type(my_age),"My age is", my_age)

# Float
result:float = 75.22
print(type(result),"Result is", result)

# Boolean
is_pass:bool = True
print(type(is_pass),"Quater 2 Result is", is_pass)

# List

skills:list[str] = ["HTML","CSS","TYPESCRIPT","JAVASCRIPT","NEXT.js","TWAILWIND CSS","REACT.JS"] 
print(type(skills),"My Skills is", skills)

num:list[int] = [2,4,6,8,10,12,14,16]
print(type(num),"number:",num)


# Dictionary
my_info:dict[str:str or int] = {
    "name": "Humaira Osama",
    "age": 32,
    "city": "Karachi",
    "is_student": True,
    "marks": 75.22
}
print(type(my_info),"My info is:",my_info)


# function 
# Favrit_food
def favrit_food(name:str, price:int):
    
    return f"{name},is my favrit food and it price is {price}"

food = favrit_food("Chicken Karahi", 500)
print(type(food), "  ", food)
 


 # Favrit_Drink
def favrit_drink(name:str, price:int):
    
    return f"{name},is my favrit drink and it price is {price}"

drink = favrit_drink("pepsi", 200)
print(type(drink), "  ", drink)