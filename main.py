import random
from game_data import data
from art import logo
from art import vs
from replit import clear

print(logo)
first = random.choice(data)
print(f'Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}')

print(vs)
second = random.choice(data)
print(f'Against B: {second["name"]}, a {second["description"]}, from {second["country"]}')

score = 0

a = first["follower_count"]
b = second["follower_count"]


game = True
while game:
    user = input("Who has more followers? Type 'A' or 'B': ")
    if (user == "A" and a > b) or (user == "B" and b > a):
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        first.update(second)
        a = b
        # print(a)
        print(f'Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}')
        second = random.choice(data)
        b = second["follower_count"]
        if first == second:
            second = random.choice(data)
            b = second["follower_count"]
        # print(b)
        print(vs)
        print(f'Against B: {second["name"]}, a {second["description"]}, from {second["country"]}')
    else:
        if (user == "A" and a < b) or (user == "B" and b < a):
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game = False
