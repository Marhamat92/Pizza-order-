print("Welcome to Marhamat's Pizza Restaurant!")
size = input("What size pizza do you want? S, M, or L ")
bill=0

if size=="S":
  bill=15
  print(f"Small pizza is ${bill}")

elif size=="M":
  bill=20
  print(f"Medium pizza is ${bill}")
  
elif size=="L":
  bill=25
  print(f"Large pizza is ${bill}")
  
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni=="Y" and size=="S":
  bill+=2
  print(f"Total bill is ${bill}")
elif add_pepperoni=="Y" and size=="M":
    bill+=3
    print(f"total bill is ${bill}")
elif add_pepperoni=="Y" and size=="L":
     bill+=3
     print(f"total bill is ${bill}")
else:
  bill+=0
  print(f"Total bill is ${bill}") 


extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese=="Y":
  bill+=1
  print(f"The final bill is ${bill}")
else:
  bill+=0
  print(f"The final bill is ${bill}")