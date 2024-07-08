#TODO: Create a letter using starting_letter.txt
letter = open("Input/Letters/starting_letter.txt","r")
letters = letter.read()
#for each name in invited_names.txt
names = open(r"Input/Names/invited_names.txt")
name=names.readlines()
for nam in name:
    stripped = nam.strip()
    result = letters.replace("[name]", f"{stripped}")
    print(result)
    with open(f"Output/ReadyToSend/letter_for_{stripped}.txt","w") as completed_letter:
        completed_letter.write(result)


#Replace the [name] placeholder with the actual name.


#Save the letters in the folder "ReadyToSend".

#
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

 # Angellas soltion

# PLACEHOLDER = "[name]"

# with open("Input/Names/invited_names.txt") as name_list:
#     names = name_list.readlines()
#
# with open("Input/Letters/starting_letter.txt") as letter_file:
#     letter_content = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
#         with open(f"Output/ReadyToSend/letter_for_{stripped_name}","w") as completed_letter:
#             completed_letter.write(new_letter)