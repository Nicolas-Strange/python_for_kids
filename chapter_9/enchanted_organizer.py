import os
import re


class Organizer:
    """
    A magical organizer to sort
    spells into different categories.
    """

    def __init__(self, path_input_file: str):
        """
        Initialize the Organizer with the path
         to the input file and a regex pattern.

        Args:
            path_input_file (str): The path to the
            input file containing spells.
        """
        self._path_input_file = path_input_file
        self._regex_cat = re.compile(r"\((\w+)\)")

    def organize(self) -> None:
        """
        Read spells from the input file,
        categorize them, and store in
        respective folders.
        """
        with open(self._path_input_file, 'r') as content:
            for row in content:
                row = row.strip()
                category = self._regex_cat.findall(row)
                if category:
                    category = category[0]
                    try:
                        os.mkdir(category)
                    except FileExistsError:
                        pass
                    path = os.path.join(category, f"{category}.txt")
                    with open(path, "a") as file:
                        file.write(f"{row}\n")


def main():
    """
    The magical entrance to the
    Organizer's spellbinding sorting.
    """
    path_input_file = "spells.txt"

    org = Organizer(path_input_file=path_input_file)
    org.organize()


if __name__ == '__main__':
    main()
