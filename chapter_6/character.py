
class Character:
    """
    Represents a magical character with a name, power level, and health.
    """
    def __init__(self, name: str, power: int, health: int):
        """
        Initializes a new magical creature.

        Parameters:
            name (str): The name of the magical creature.
            power (int): The power level of the magical creature.
            health (int): The health level of the magical creature.
        """
        self.name = name
        self.power = power
        self.health = health

    def cast_spell(self) -> int:
        """
        Casts a spell and returns the power level of the spell.

        Returns:
            int: The power level of the spell.
        """
        return self.power
