# Automated-Letter-Generation
This project is a simple script that generates personalized letters for a list of names using a template letter.

# How it Works
The script reads a list of names from a file called invited_names.txt in the Input/Names directory.
It then reads a template letter from a file called starting_letter.txt in the Input/Letters directory.
For each name in the list, the script replaces the [name] placeholder in the template letter with the actual name.
The resulting personalized letter is then saved as a new file in the Output/ReadyToSend directory, with the name letter_for_<name>.txt.

# Code Explanation
The code uses the following Python concepts:

File input/output: The script reads from and writes to files using the open function.
String manipulation: The script uses the replace method to replace the [name] placeholder with the actual name, and the strip method to remove whitespace from the names.
Looping: The script uses a for loop to iterate over the list of names.

# Files and Directories
The script assumes the following file and directory structure:

Input/Names/invited_names.txt: A file containing a list of names, one per line.
Input/Letters/starting_letter.txt: A file containing the template letter.
Output/ReadyToSend/: A directory where the personalized letters will be saved.
