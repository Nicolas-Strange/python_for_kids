# List of magical artifacts that the user can choose from
artifacts = [
    'Gravitatis Imperium',
    'Communicatio Animalis',
    'vacuus orbis'
]

# Introduction and instructions for the user
print(
    "Hello, young wizard! My name is Lyranthra. \n"
    "If you want my artifact, you will have to prove your worth \n"
    "by defeating me with your power. Let's begin!\n"
)

# Health of the opponent
lyranthra_health = 100

# Main game loop that runs while
# the opponent still has health
while lyranthra_health > 0:
    print("\nChoose your artifact:")

    # Print out all available artifacts
    for index, artifact in enumerate(artifacts):
        print(f"{index + 1}: {artifact}")

    # User inputs their choice of artifact
    choice = input("Enter a number: ")

    # Implement the effect of each artifact
    if choice == "1":  # Gravitatis Imperium
        damages = 20
        print(
            "\nYou concentrate your power \n"
            "to lift a mountain into the air \n"
            "with Gravitatis Imperium and \n"
            "throw it at Lyranthra.\n"
            f"You deal {damages} damage!\n"
        )

        # Reduce opponent's health
        lyranthra_health -= damages

    elif choice == "2":  # Communicatio Animalis
        print(
            "\nYou look around you to find an animal. \n"
            "But the only animal you see is a skinny frog. \n"
            "You try to convince the frog with \n"
            "Communicatio Animalis to attack Lyranthra \n"
            "but no way! Replies the frog.\n"
        )
        continue  # This choice doesn't deal any damage,
        # so skip to the next loop iteration

    elif choice == "3":  # vacuus orbis
        print(
            "\nYou summon a black hole that sucks Lyranthra in. \n"
            "You feel a little bit stupid because \n"
            "the artifact you wanted is gone \n"
            "with him.\n¯\_(ツ)_/¯\n"
        )
        break  # This choice ends the game,
        # so break out of the loop
    else:
        continue  # If an invalid choice was made,
        # skip to the next loop iteration

    # After each choice, print out
    # the remaining health of the opponent
    if lyranthra_health > 0:
        print(
            "That was very powerful, \n"
            f"but I still have \n"
            f"{lyranthra_health} health left.\n"
            "You will have to do better!\n"
        )
    else:
        print(
            "I have to admit you have strong powers. \n"
            "You won! You deserve my artifact, take it."
        )
