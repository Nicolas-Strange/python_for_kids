class MagicalCreature:
    def __init__(self, creature_type: str, power_level: int, health_points: int):
        """
        Initialize a magical creature with its type, power level, and health points.

        Args:
            creature_type (str): The type of the magical creature.
            power_level (int): The power level of the magical creature.
            health_points (int): The health points of the magical creature.
        """
        self.creature_type = creature_type
        self.power_level = power_level
        self.health_points = health_points


def cast_spell(creature: MagicalCreature) -> int:
    """
    Casts a spell based on the power level of the magical creature.

    Args:
        creature (MagicalCreature): The magical creature whose power level determines the spell damage.

    Returns:
        int: The spell damage based on the creature's power level.
    """
    return creature.power_level


def battle_wizard(wizard: MagicalCreature, creature: MagicalCreature) -> None:
    """
    Simulates a battle between a wizard and a magical creature.

    Args:
        wizard (MagicalCreature): The wizard involved in the battle.
        creature (MagicalCreature): The magical creature involved in the battle.
    """
    wizard_health = wizard.health_points
    creature_health = creature.health_points

    while wizard_health > 0 and creature_health > 0:
        wizard_damage = cast_spell(wizard)
        creature_damage = cast_spell(creature)

        wizard_health -= creature_damage
        creature_health -= wizard_damage

    if wizard_health <= 0:
        print("Oh no! The wizard has been defeated.")
    else:
        print("Congratulations! The wizard defeated the", creature.creature_type)


def main() -> None:
    wizard_name = input("Enter your wizard's name: ")
    wizard_power = int(input("Enter your wizard's power level (1-10): "))
    wizard_health = int(input("Enter your wizard's health points (1-50): "))

    wizard = MagicalCreature(wizard_name, wizard_power, wizard_health)

    creatures = [
        MagicalCreature("Goblin", 4, 15),
        MagicalCreature("Dragon", 8, 30),
        MagicalCreature("Fairy", 5, 20)
    ]

    for creature in creatures:
        print("\nA", creature.creature_type, "has appeared!")
        choice: str = input("Do you want to (b) battle or (r) run? ").lower()

        if choice == "b":
            battle_wizard(wizard, creature)
        elif choice == "r":
            print("You run away from the", creature.creature_type)
        else:
            print("Invalid choice! The", creature.creature_type, "attacks while you hesitate!")


if __name__ == "__main__":
    main()
