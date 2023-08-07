from character import Character


def battle_wizard(wizard: Character, creature: Character) -> None:
    """
    Simulates a battle between a wizard and a magical creature.

    Parameters:
        wizard (Character): The wizard.
        creature (Character): The magical creature.
    """
    print(f"A wild {creature.name} has appeared! Prepare for battle!")
    turn_count = 1
    while wizard.health > 0 and creature.health > 0:
        print(f"######### TURN {turn_count} #########")
        wizard_damage = wizard.cast_spell()
        creature_damage = creature.cast_spell()

        print(f"{wizard.name} casts a spell with power {wizard_damage}.")
        print(f"{creature.name} counters with a spell of power {creature_damage}.")

        wizard.health -= creature_damage
        creature.health -= wizard_damage

        print(f"{wizard.name}'s health: {wizard.health}")
        print(f"{creature.name}'s health: {creature.health}\n")

        turn_count += 1

    if wizard.health <= 0:
        print("Oh no! The wizard has been defeated.")
    else:
        print(f"Congratulations! {wizard.name} defeated the {creature.name}!")
