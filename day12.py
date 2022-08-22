# Scope

# Global Scope
player_health = 10

def game():
    def drink_portion():
        potion_strength = 2 # Local Scope
        print(player_health)
    
    drink_portion()

print(player_health)

# Python does not have block scope

# Modifying Global Scope
enemies = 1

def increase_enemies():
    # global enemies # makes this global variable accessible inside the local scope
    print(f"enemies outside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants
# Uppercase variables are constants
PI = 3.14159
URL = "https://www.google.com"