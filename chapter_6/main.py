from random import randint

from battle import battle_wizard
from character import Character


def main() -> None:
    """
    The main function to run the magical creature battle game.
    """
    print("Welcome to the Magical Creature Battle Game!")
    wizard_name = input("Enter your wizard's name: ")

    wizard = Character(
        name=wizard_name,
        power=randint(10, 20),
        health=randint(10, 100)
    )

    creatures = [
        Character(
            name="Goblin",
            power=randint(5, 10),
            health=randint(10, 100)
        ),
        Character(
            name="Dragon",
            power=randint(15, 25),
            health=randint(10, 100)
        ),
        Character(
            name="Fairy",
            power=randint(10, 100),
            health=randint(10, 100)
        )
    ]

    for creature in creatures:
        choice = input(f"Do you want to summon {creature.name}? (y/n): ").lower()

        if choice == "y":
            battle_wizard(wizard, creature)
        else:
            print(f"You decide not to summon {creature.name}.")
            print("The battle continues with the next creature.\n")


if __name__ == "__main__":
    main()
