# Introduction of the magic scroll
print(
    "Greetings, young wizard! \n"
    "I can sense your curiosity and passion for knowledge. \n"
    "Within me lies a treasure trove of wisdom, waiting to be unlocked. \n"
)

# Ask the name to the wizard
name = input("What is your name young wizard?\n")

# The magic scroll uses the variable name to insert it into the text
print(
    f"\nBefore I reveal to you my secret {name}, \n"
    "you must embark on a quest to discover the magical password. \n"
    "Are you ready for an enchanting adventure?\n\n"
    "Pay close attention and answer my question to reveal the hidden word.\n"
)

# The magic scroll poses a question to the wizard using an input.
print("***************************************************")
password = input("I grow and flourish, nourishing seekers of wisdom. "
                 "What am I?\n")

# Create a condition to verify the password
# If the password is correct, this block is executed
if password == "knowledge":
    print(f"Well done, {name}!\n"
          "You found the secret word to reveal my knowledge.\n"
          "I am going to give you a tip to become a better Pythonist wizard. Listen carefully!\n\n"
          "In Python, indentation is like special spacing that organizes code.\n"
          "It helps Python understand which lines belong together,\n"
          "just like paragraphs in a story.\n\n")

    print("You can now continue your journey to discover more knowledge \n"
          "and become the greatest Pythonist wizard of all time!")

# If the password is not correct, this block is executed
else:
    print("Not correct! You need to enhance your knowledge to gain access to the truth.")
