# Caesar Cipher Encryption Tool

Author: Girdhar

Internship Task 2 - CodeOrbit Tech (Cyber Security Internship)

A simple Python program that encrypts and decrypts text using the Caesar Cipher technique. The user can choose the shift value (key), and both the encrypted and decrypted output are shown clearly.

## Technologies Used

- Python 3 (no external libraries)

## What Is the Caesar Cipher?

It is one of the oldest and simplest encryption methods. Every letter is moved forward by a fixed number called the key.

Example with key 3: `A -> D`, `B -> E`, `Z -> C`

So `Hello` becomes `Khoor`. To decrypt, the letters are moved backward by the same key.

## Features

- Encrypt a message with a key of your choice (1 to 25)
- Decrypt a message with the same key
- Shows the original, encrypted, and decrypted text clearly
- Keeps uppercase and lowercase letters correct
- Numbers, spaces, and symbols stay the same
- Checks that the key is a valid number

## Setup Instructions

1. Install Python 3 from https://www.python.org
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run: `python caesar_cipher.py`
5. Choose an option from the menu and follow the instructions

## Example

```
Enter the text to encrypt: Hello World
Enter shift value / key (1-25): 3

  Original    : Hello World
  Key         : 3
  Encrypted   : Khoor Zruog
  Decrypted   : Hello World
```

## GitHub Repository Link

Add your repository link here: `https://github.com/<your-username>/<repo-name>`
