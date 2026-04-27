# password_checker.py
This Python project is a Password Strength Checker designed to evaluate the security of user‑entered passwords. It applies multiple validation rules to ensure that passwords meet basic cybersecurity standards. The tool checks for:

Minimum length of 8 characters

Presence of at least one digit

Presence of lowercase and uppercase letters

Inclusion of special characters (!@#$%^&*(){<>?})

Avoidance of very common weak passwords (e.g., Admin, Password, abc123, etc.)

The program runs in a simple command‑line interface where users can repeatedly test passwords until they type "exit". Based on the checks, it classifies passwords as Weak, Medium, or Strong, and provides feedback on how to improve them.


HOW TO RUN:
Save the script as password_checker.py.

Run it in a terminal:

bash
python password_checker.py
Enter passwords to test their strength.
Type exit to quit the program.
