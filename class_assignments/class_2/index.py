
#     ***====***  Arithmetic operators  ***====***
print("=====Arithmetic operators=====")

a = 32 
b = 3
c = 200
d = 49


# 1. Adidition  (+)
add = a + b
print(add)   #  result = 35



# 2. Subtraction  (-)
sub = a - b
print(sub)  #  result = 29


# 3. Multiplcation  (*)
miltipy = a * b
print(miltipy)  #  result = 96


# 4. Division  (/)
divide = c / b
print(divide)  #  result = 66.666666666



# 5. Floor Division  (//)
# Ye bhi division karta hai, lekin decimal (point) hata deta hai aur integer return karta hai.
floor_division = c // b
print(floor_division)  #  result = 66


# 6. Modulus  (%) 
# Ye division ka remainder return karta hai.
modulus = c % d
print(modulus)  #  result = 4


# 7. Exponent  (**) 
Exponent = b ** 3
print(Exponent)  #  result = 27




print("=====Assignment operators=====")
#     ***====***  Assignment operators  ***====***

# 1. assign  (=)
num = 5  # num me 5 ko assign kia gya h


# 2. Addition and Assign  (+=)
a += b
print(a)  #  result = 35


# 3. Subtraction and assign  (-=)
a -= b
print(a)  #  result = 32


# 4. Multiplcation and Assign  (*=)
a *= b
print(a)  #  result = 96


# 5. Division and Assign (/=)
c /= b
print(c)  #  result = 66.666666666



# 6. Floor Division and Assign (//=)
c = 200
c //= b
print(c)  #  result = 66


# 7. Modulus and Assign (%=) 
c = 200
c %= d
print(c)  #  result = 4


# 8. Exponent and Assign  (**=) 
b **= 3
print(b)  #  result = 27





print("=====Comparison operators=====")
#     ***====***  Comparison operators  ***====***

x = 10
y = 5

# 1. Equal to (==)
print(x == 10)  # True
print(x == y)   # False

# 2. Not equal to (!=)
print(x != y)   # True
print(x != 10)  # False

# 3. Greater than (>)
print(x > y)    # True
print(y > x)    # False

# 4. Less than (<)
print(y < x)    # True
print(x < 5)    # False

# 5. Greater than or equal to (>=)
print(x >= 10)  # True
print(y >= 10)  # False

# 6. Less than or equal to (<=)
print(y <= 5)   # True
print(x <= 5)   # False





print("=====Logical operators=====")
#     ***====***  Logical operators  ***====***

x = 15
y = 10
z = 20

# 1. AND Operator (Dono True honi chahiye)
print((x > y) and (z > x))  # True 
print((x > y) and (z < x))  # False

# 2. OR Operator (Aik bhi True ho to result True)
print((x > y) or (z < x))   # True 
print((x < y) or (z < x))   # False 

# 3. NOT Operator (Condition ko ulta kar deta hai)
print(not(x > y))  # False 
print(not(x < y))  # True 





print("=====identify operators=====")
#     ***====***  Identify operators  ***====***

# Variables
a = 5
b = 5
c = 5.0

# 1. Using 'is'
print(a is b)   # True 
print(a is c)   # False 

# 2. Using is not'
print(a is not c)  # True 




print("=====membership operators=====")
#     ***====***  membership operators  ***====***

text = "Humaira Osama!"

print("H" in text)     # True  ("H" mojood hai)
print("b" in text)     # False ("b" nahi hai)
print("Osama" in text) # True  (Complete word bhi check hota hai)
print("osama" in text) # False (Case-sensitive)

