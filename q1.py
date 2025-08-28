import string

# Constants for alphabets
LOWER_FIRST_HALF = set("abcdefghijklm")
LOWER_SECOND_HALF = set("nopqrstuvwxyz")
UPPER_FIRST_HALF = set("ABCDEFGHIJKLM")
UPPER_SECOND_HALF = set("NOPQRSTUVWXYZ")


def encrypt_char(c, shift1, shift2):
    if c.islower():
        if c in LOWER_FIRST_HALF:
            shift = shift1 * shift2
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif c in LOWER_SECOND_HALF:
            shift = shift1 + shift2
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
    elif c.isupper():
        if c in UPPER_FIRST_HALF:
            shift = shift1
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        elif c in UPPER_SECOND_HALF:
            shift = shift2 ** 2
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    else:
        return c  # Non-alphabetic characters remain unchanged


def decrypt_char(c, shift1, shift2):
    if c.islower():
        if c in LOWER_FIRST_HALF:
            shift = shift1 * shift2
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif c in LOWER_SECOND_HALF:
            shift = shift1 + shift2
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif c.isupper():
        if c in UPPER_FIRST_HALF:
            shift = shift1
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        elif c in UPPER_SECOND_HALF:
            shift = shift2 ** 2
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
    else:
        return c


def encrypt_file(input_path, output_path, shift1, shift2):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            encrypted_line = ''.join(encrypt_char(c, shift1, shift2) for c in line)
            outfile.write(encrypted_line)


def decrypt_file(input_path, output_path, shift1, shift2):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            decrypted_line = ''.join(decrypt_char(c, shift1, shift2) for c in line)
            outfile.write(decrypted_line)


def verify_decryption(original_path, decrypted_path):
    with open(original_path, 'r', encoding='utf-8') as original, \
         open(decrypted_path, 'r', encoding='utf-8') as decrypted:
        original_content = original.read()
        decrypted_content = decrypted.read()

        if original_content == decrypted_content:
            print("✅ Decryption successful: Original and decrypted files match.")
        else:
            print("❌ Decryption failed: Files do not match.")


def main():
    # Prompt user for shift values
    try:
        shift1 = int(input("Enter shift1 (integer): "))
        shift2 = int(input("Enter shift2 (integer): "))
    except ValueError:
        print("Shift values must be integers.")
        return

    # File paths
    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    # Process
    encrypt_file(raw_file, encrypted_file, shift1, shift2)
    decrypt_file(encrypted_file, decrypted_file, shift1, shift2)
    verify_decryption(raw_file, decrypted_file)


if __name__ == "__main__":
    main()
