# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.docx") as letter:
    letter_text = letter.read()

for name in names_list:
    stripped_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as mail:
        customized_letter = letter_text.replace(PLACEHOLDER, stripped_name)
        mail.write(customized_letter)
