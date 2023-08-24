from typing import List, Dict


class Monster:
    def __init__(self, name: str, power: int, loot: str):
        """
        Initialize a Monster instance.

        Parameters:
            name (str): The name of the monster.
            power (int): The power level of the monster.
            loot (str): The loot dropped by the monster.
        """
        self.name = name
        self.power = power
        self.loot = loot


def main():
    """
    The main function to play the Monster Hunter Quest game.
    """
    regions: Dict[str, List[Monster]] = {
        "Forest": [
            Monster("Goblin", 20, "Gold"),
            Monster("Wolf", 30, "Fur"),
        ],
        "Cave": [
            Monster("Orc", 40, "Gem"),
            Monster("Bat", 15, "Wing"),
        ],
        "Mountain": [
            Monster("Dragon", 100, "Treasure"),
            Monster("Yeti", 50, "Claw"),
        ]
    }

    collected_loot: List[str] = []

    print("Welcome to the Monster Hunter Quest!")
    print("You'll travel through different regions to hunt monsters and collect their loot.")

    while True:
        print("\nAvailable regions:")
        for region in regions.keys():
            print(region)

        selected_region = input("\nEnter the name of the region you want to explore (or 'quit' to exit): ")

        if selected_region.lower() == 'quit':
            print("Thank you for playing the Monster Hunter Quest!")
            break

        if selected_region in regions:
            print(f"\nYou entered the {selected_region}. Get ready to face some monsters!")
            monsters_in_region = regions[selected_region]

            for monster in monsters_in_region:
                print(f"\nA wild {monster.name} appears!")
                choice = input("Do you want to fight? (yes/no): ")

                if choice.lower() == 'yes':
                    if monster.power >= 50:
                        print(f"Uh-oh! The {monster.name} is too powerful. You were defeated!")
                        print("Game Over.")
                        return

                    print(f"You defeated the {monster.name} and gained {monster.loot}.")
                    collected_loot.append(monster.loot)
                else:
                    print(f"You decided not to fight the {monster.name}.")

            print(f"\nCongratulations! You collected the following loot: {', '.join(collected_loot)}")
        else:
            print("Sorry, that region doesn't exist in our world.")


if __name__ == "__main__":
    main()
