# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Could also write:  name = input("What's your name?  ").strip().title()

# Print the output
print(f"Hello, {name}")
