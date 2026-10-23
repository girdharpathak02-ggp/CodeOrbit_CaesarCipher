# Caesar Cipher Encryption Tool
# Author: Girdhar
# Internship Task 2 - CodeOrbit Tech (Cyber Security)
# This program encrypts and decrypts text using the Caesar Cipher.
# Caesar Cipher = every letter is moved forward by a fixed number (the key).
# Example: key = 3  ->  A becomes D, B becomes E, Z becomes C


def line(char="-", size=56):
    print(char * size)


def show_banner():
    line("=")
    print("*" * 56)
    print("*" + "CAESAR CIPHER TOOL".center(54) + "*")
    print("*" + "Made by Girdhar".center(54) + "*")
    print("*" * 56)
    line("=")


def show_how_it_works():
    print("\n+" + "-" * 54 + "+")
    print("|" + "  HOW IT WORKS".ljust(54) + "|")
    print("+" + "-" * 54 + "+")
    print("|" + "  Each letter moves forward by the KEY (shift).".ljust(54) + "|")
    print("|" + "  Example with key 3:  A -> D,  B -> E,  Z -> C".ljust(54) + "|")
    print("|" + "  To decrypt, move the letters backward.".ljust(54) + "|")
    print("|" + "  Numbers and symbols stay the same.".ljust(54) + "|")
    print("+" + "-" * 54 + "+")


def shift_text(text, shift):
    # moves every letter by the shift value
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch   # numbers, spaces and symbols stay same
    return result


def encrypt(text, key):
    return shift_text(text, key)


def decrypt(text, key):
    return shift_text(text, -key)


def get_key():
    # keeps asking until the user enters a number from 1 to 25
    while True:
        key = input("Enter shift value / key (1-25): ")
        if key.isdigit() and 1 <= int(key) <= 25:
            return int(key)
        print("  [!] Please enter a number between 1 and 25.")


def show_result(title, rows):
    print()
    line("=")
    print("  " + title)
    line("=")
    for label, value in rows:
        print("  " + label.ljust(12) + ": " + value)
    line("=")


def do_encrypt():
    print()
    line("-")
    text = input("Enter the text to encrypt: ")
    if text == "":
        print("  [!] Text cannot be empty.")
        return
    key = get_key()
    line("-")

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)   # decrypt again to prove it works

    show_result("ENCRYPTION RESULT", [
        ("Original", text),
        ("Key", str(key)),
        ("Encrypted", encrypted),
        ("Decrypted", decrypted),
    ])
    if decrypted == text:
        print("  [+] Success! Decrypted text matches the original.")


def do_decrypt():
    print()
    line("-")
    text = input("Enter the text to decrypt: ")
    if text == "":
        print("  [!] Text cannot be empty.")
        return
    key = get_key()
    line("-")

    decrypted = decrypt(text, key)

    show_result("DECRYPTION RESULT", [
        ("Encrypted", text),
        ("Key", str(key)),
        ("Decrypted", decrypted),
    ])


def main():
    show_banner()
    show_how_it_works()

    while True:
        print("\n  MENU")
        line("-", 20)
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Exit")
        line("-", 20)
        choice = input(">> Choose an option (1-3): ")

        if choice == "1":
            do_encrypt()
        elif choice == "2":
            do_decrypt()
        elif choice == "3":
            print("\n  Goodbye! Stay safe online.")
            line("=")
            break
        else:
            print("  [!] Invalid choice. Please enter 1, 2 or 3.")


main()
