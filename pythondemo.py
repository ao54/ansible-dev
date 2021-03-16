resp= input("Is Ansible awesome, yes or no?")


### conditional with lower() and strip() python methods for white characters/spaces
if resp.lower().strip() =="yes":
   print( "Yes, Ansible is awesome!")
elif resp.lower().strip() == "no":
    print("You have no idea")

else:
    print("Wrong input")

