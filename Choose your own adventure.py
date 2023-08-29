# Day 3 final project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
choice1 = input("Which direction would you like to travel? Left or Right? ")

if choice1 == "Left".lower():
    choice2 = input("You come across a large body of water. Do you risk it and swim across, or stay patient and wait? Swim or Wait. ")
    
    if choice2 == "Wait".lower():
        choice3 = input("Your patience has paid off, Traveler. Finally, you must choose a door. Let us hope that you make the correct choice. Blue, Yellow, or Red? ")
    
        if choice3 == "Yellow".lower():
            print("Congratulations, Traveler. You have won the treasure you seek. ")
        elif choice3 == "Red".lower():
            print("You open the door and are immediately consumed by the raging fires that burst forth across the threshold. Game over. ")
        elif choice3 == "Blue".lower():
            print("The door opens revealing a crouched beast ready to pound on their unsuspecting prey. Game over. ")
        else:
            print("Game over. ")
    else:
        print("Your gamble to make the swim has not paid off. You have been eaten by giant river trout. Game over. ")
else:
    print("You take a step and fall 20 feet into a boobietrapped pit. Game over. ")