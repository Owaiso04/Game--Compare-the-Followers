import random
import data

logo_1 = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
/ /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/      
"""

logo_2 = """
 _    __    
| |  / /____
| | / / ___/
/ |/ (__  ) 
|___/____(_)
"""

print(logo_1)

# Initial random selection ensuring distinct comparisons
Compare_A = data.data[random.randint(0, 49)]
Compare_B = data.data[random.randint(0, 49)]
while Compare_B == Compare_A:
    Compare_B = data[random.randint(0, 49)]

count = 0

# Game Loop
while True:
    print("\n" * 20)
    # Display current comparison
    print(
        f"Compare A: {Compare_A['name']}, {Compare_A['description']}, from {Compare_A['country']}"
    )
    print(logo_2)
    print(
        f"Compare B: {Compare_B['name']}, {Compare_B['description']}, from {Compare_B['country']}"
    )

    # User input
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Determine if the answer is correct and update accordingly
    if answer == "a" and Compare_A["followers_count"] >= Compare_B["followers_count"]:
        count += 1
        print(f"You're right! Current score: {count}")
        Compare_B = data.data[
            random.randint(0, 49)
        ]  # New random comparison while keeping Compare_A
    elif answer == "b" and Compare_B["followers_count"] >= Compare_A["followers_count"]:
        count += 1
        print(f"You're right! Current score: {count}")
        Compare_A = data.data[
            random.randint(0, 49)
        ]  # New random comparison while keeping Compare_B
    else:
        # Game over condition
        print(f"Sorry, that's wrong. Final score: {count}")
        break
