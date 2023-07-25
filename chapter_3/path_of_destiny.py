# Create the variables for the answers
print("Long ago, the Mystorians, an advanced race from space,"
      " created Mystoria, a magnificent planet.")
print("They introduced the Humans, "
      "a species crafted in their image using magic, "
      "to the world of Mystoria.")
print("The Humans possessed remarkable abilities "
      "to learn and adapt quickly.")

# Player's choice
print("As you venture through the magical realm of Mystoria, "
      "you find a mysterious roll.")
print("Would you like to attempt to decrypt it?")

choice = input("Enter '1' for yes or '2' to continue "
               "without paying attention to it: ")

print("\n")
# First condition
if choice == "1":
    print("As you touch the scroll, it starts emitting "
          "mysterious lights and strange symbols appear on its surface. "
          "You are unable to decipher the symbols, but below them, "
          "a sentence that you can understand presents you with a riddle.")
    print("This riddle is said to reveal a secret "
          "power hidden deep within Mystoria.")

    print("The riddle on the scroll appears before you:")
    print("I am a number between 1 and 10. "
          "If you multiply me by 3 and subtract 5, the result is 16. "
          "What number am I?")

    # Player's answer
    answer = input("Enter your answer: ")
    print("\n")
    # Riddle condition
    if int(answer) * 3 - 5 == 16:
        print("Congratulations! You've solved the riddle "
              "and unlocked the ancient power of Mystoria.")

        print("With your newfound power, "
              "you can read the mysterious symbols on the scroll")
        print("These symbols unveil the location of the ancient artifacts of power "
              "and a curious secret that you will keep to yourself.")

    else:
        print("Oops! That's not the correct answer.")
        print("Suddenly, the air around you crackles with magic.")
        print("The ancient scroll bursts into brilliant "
              "flames, illuminating the surroundings.")
        print("As the flames dance and swirl, the scroll "
              "transforms into shimmering embers and "
              "vanishes into thin air.")
        print("The presence of the ancient knowledge lingers, "
              "leaving you with a sense of mystery and intrigue.")

elif choice == "2":
    print("You stand at the crossroads, your heart "
          "filled with curiosity and a thirst for adventure.")
    print("As the mystical scroll glimmers before you,"
          " an invitation to unravel its secrets, you hesitate.")
    print("The decision weighs on you, torn between "
          "the allure of the unknown and the safety of familiarity.")

    print("In the depths of your being, "
          "a whisper of regret emerges, "
          "questioning the path untaken.")
    print("But as you turn your gaze back to the spot "
          "where the scroll once lay, a sense of "
          "mystery fills the air.")
    print("The scroll has vanished, leaving you with "
          "an enigma that will forever remain unanswered.")

    print("Yet, in the realm of magic and mystique, "
          "every choice leads to new discoveries.")
    print("You continue your journey, embracing the uncertainty,"
          " and embracing the endless possibilities "
          "that lie ahead in the enchanting world of Mystoria.")

else:
    print("Invalid choice. Please enter a valid option.")
