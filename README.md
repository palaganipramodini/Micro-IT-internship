# Micro-IT-internship
Description of the Password Generator Script
This Python program generates a secure, random password based on a user-specified length.

How it works step-by-step:
Imports necessary modules:

random — to pick random characters and shuffle the password.

string — provides predefined sets of characters (lowercase, uppercase, digits, symbols).

Function generate_password(length=12):

Takes the desired password length (default is 12).

Checks if the length is at least 4 (minimum to include one of each character type).

Defines character sets:

Lowercase letters (a-z)

Uppercase letters (A-Z)

Digits (0-9)

Symbols (punctuation like !@#$%&*)

Ensures password contains at least one character from each category to increase strength.

Fills the remaining length with a random selection from all categories combined.

Shuffles the characters to avoid predictable patterns.

Returns the final password as a string.

Main program (main() function):

Prints a header message.

Prompts the user to enter the desired password length.

Validates input to make sure it is a number and at least 4.

Calls generate_password() with the input length.

Prints the generated password or shows an error message for invalid input.

Execution entry point:

When the script runs directly (not imported), it calls main().
