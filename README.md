# Secure-Credential-and-Authentication-Utility
Allows the user to either generate a strong password, verify the strength of their password, or use multi authentication 



Secure Credential and Authentication Utility

💡 Overview

This Python utility provides a comprehensive set of tools for managing and enhancing digital security. It includes a cryptographically secure password generator, a robust password strength verifier, and a Time-based One-Time Password (TOTP) implementation for simulating Multi-Factor Authentication (MFA) logins.

The program is designed to be run from the command line, offering a simple menu for accessing all security features.

🚀 Features

1. Password Generation (gen)

Cryptographically Secure: Utilizes Python's secrets module for generating strong, unpredictable passwords.

Customizable Length: Allows the user to specify the desired password length (default is 16 characters).

Symbol Inclusion: Option to include a broad range of special symbols.

Similar Character Exclusion: Option to exclude characters that look similar (e.g., 'l', '1', 'I', 'O', '0') to improve readability and reduce entry errors.

2. Password Strength Verification (ver)

Robust Scoring: Calculates a strength score based on length, and the presence of uppercase, lowercase, digits, and symbols.

Feedback: Provides clear feedback on strength: "Very Strong," "Moderate," or "Weak," with specific recommendations for improvement.

3. Multi-Factor Authentication (MFA) Login (mfa)

TOTP Implementation: Generates a 6-digit Time-based One-Time Password (TOTP) using the HMAC-SHA256 algorithm.

Time Sensitivity: Simulates a 30-second window for password entry. If the user enters the OTP after the time limit, the authentication fails.

🛠️ Requirements

This program relies solely on standard Python libraries and has no external dependencies.

Python: 3.6+

Standard Libraries Used:

secrets

string

time

hmac

hashlib

💻 How to Run

Save the Python code as security_utility.py.

Run the script from your terminal:

python security_utility.py


The program will present a menu:

Select One of the Following Options:
Password Generation
Verify Your Passwords Strength
Multi-Factor Authentication Login
Exit


Enter the corresponding command for your choice:

Menu Option

Command to Enter

Description

Password Generation

gen

Generates a new secure password.

Verify Your Passwords Strength

ver

Checks the strength of an existing password.

Multi-Factor Authentication Login

mfa

Runs the TOTP demonstration.

Exit

done

Closes the program.
