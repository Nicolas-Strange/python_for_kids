# Wizard Game

# Welcome the player to the game
print("Welcome, young wizard!")

# Ask the player for their wizard name
wizard_name = input("What is your wizard name? ")

# Greet the player by their wizard name with an air of mystery
print("Greetings, " + wizard_name + "! Prepare to embark on a grand magical adventure!")

# Ask the player for their age
wizard_age = int(input("How old are you, " + wizard_name + "? "))

# Check if the player is old enough to play the game
if wizard_age >= 18:
    print("You possess remarkable wisdom and power, " + wizard_name + "! Let the enchantment begin!")

    # Ask the player for a magic number
    magic_number = int(input("Enter a magic number: "))

    # Perform an operation on the magic number
    result = magic_number * 2

    # Convert the result to a string
    result_str = str(result)

    # Create a magic spell based on the player's name and the result
    magic_spell = wizard_name + ", the mystical forces reveal your enchanted number: " + result_str

    # Display the magic spell with captivating effects
    print("Prepare to witness the manifestation of magic...")
    print("*~*~*~*~*~*~*~*~*~*")
    print("~~~ MAGICAL SPELL ~~~")
    print("*~*~*~*~*~*~*~*~*~*")
    print(magic_spell)
    print("*~*~*~*~*~*~*~*~*~*")
    print("~~~ END OF SPELL ~~~")
    print("*~*~*~*~*~*~*~*~*~*")

    print("Embrace your destiny, mighty " + wizard_name + "!")
    print("May your magical journey be filled with wonders and triumphs!")
else:
    print("Apologies, " + wizard_name + ". To unveil the depths of your sorcery, you must be at least 18 years old.")

# End the game with a sense of fulfillment and wonder
print("Farewell, " + wizard_name + "! May the cosmos align in your favor, and may your magic forever shine brightly!")
