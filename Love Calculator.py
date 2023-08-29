print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
comb_names = (name1 + name2).lower()

comb_names.count("t")
comb_names.count("r")
comb_names.count("u")
comb_names.count("e")
true = int(comb_names.count("t") + comb_names.count("r") + comb_names.count("u") + comb_names.count("e"))

comb_names.count("l")
comb_names.count("o")
comb_names.count("v")
comb_names.count("e")
love = int(comb_names.count("l") + comb_names.count("o") + comb_names.count("v") + comb_names.count("e"))

score = int(f"{true}{love} ")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together. ")
else:
    print(f"Your score is {score}, there is no magic formula for the perfect relationship. It takes hard work and patience. ")