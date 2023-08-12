print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_one = name1.lower()
name_two = name2.lower()

t = name_one.count('t') 
r = name_one.count('r') 
u = name_one.count('u') 
e = name_one.count('e') 
true_ttl1 = t + r + u + e


l = name_one.count('l') 
o = name_one.count('o') 
v = name_one.count('v') 
e = name_one.count('e') 
love_ttl1 = l + o + v + e

t = name_two.count('t') 
r = name_two.count('r') 
u = name_two.count('u') 
e = name_two.count('e') 
true_ttl2 = t + r + u + e


l = name_two.count('l') 
o = name_two.count('o') 
v = name_two.count('v') 
e = name_two.count('e') 
love_ttl2 = l + o + v + e

love_score = int(str(true_ttl1 + true_ttl2) + str(love_ttl1 + love_ttl2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


