import os

# Constants for character groups
LOWER_FIRST_HALF = set("abcdefghijklm")
LOWER_SECOND_HALF = set("nopqrstuvwxyz")
UPPER_FIRST_HALF = set("ABCDEFGHIJKLM")
UPPER_SECOND_HALF = set("NOPQRSTUVWXYZ")


def encrypt_char(c, shift1, shift2):
    """
    Encrypt a single character based on the encryption rules.
    
    Rules:
    - Lowercase first half (a-m): shift forward by shift1 * shift2
    - Lowercase second half (n-z): shift backward by shift1 + shift2
    - Uppercase first half (A-M): shift backward by shift1
    - Uppercase second half (N-Z): shift forward by shift2²
    - Other characters: unchanged
    """
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
    
    # Return unchanged for non-alphabetic characters
    return c


def decrypt_char(c, shift1, shift2):
    """
    Decrypt a single character by reversing the encryption rules.
    """
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
    
    # Return unchanged for non-alphabetic characters
    return c


def encrypt_file(input_path, output_path, shift1, shift2):
    """
    Encrypt the contents of input_path and write to output_path.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as infile, \
             open(output_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                encrypted_line = ''.join(encrypt_char(c, shift1, shift2) for c in line)
                outfile.write(encrypted_line)
        print(f"✅ File encrypted successfully: {input_path} → {output_path}")
    except FileNotFoundError:
        print(f" Error: File '{input_path}' not found.")
    except Exception as e:
        print(f" Error during encryption: {e}")


def decrypt_file(input_path, output_path, shift1, shift2):
    """
    Decrypt the contents of input_path and write to output_path.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as infile, \
             open(output_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                decrypted_line = ''.join(decrypt_char(c, shift1, shift2) for c in line)
                outfile.write(decrypted_line)
        print(f" File decrypted successfully: {input_path} → {output_path}")
    except FileNotFoundError:
        print(f" Error: File '{input_path}' not found.")
    except Exception as e:
        print(f" Error during decryption: {e}")


def verify_decryption(original_path, decrypted_path):
    """
    Compare the original file with the decrypted file to verify successful decryption.
    """
    try:
        with open(original_path, 'r', encoding='utf-8') as original, \
             open(decrypted_path, 'r', encoding='utf-8') as decrypted:
            original_content = original.read()
            decrypted_content = decrypted.read()

            if original_content == decrypted_content:
                print(" Decryption verification PASSED: Original and decrypted files match perfectly!")
                return True
            else:
                print(" Decryption verification FAILED: Files do not match.")
                print(f"Original length: {len(original_content)}, Decrypted length: {len(decrypted_content)}")
                return False
    except FileNotFoundError as e:
        print(f" Error during verification: {e}")
        return False


def create_raw_text_file_if_missing(filepath):
    """
    Create the raw text file if it doesn't exist, with user input.
    """
    if not os.path.exists(filepath):
        print(f"📄 '{filepath}' not found. Let's create it!")
        print("Enter the content you want to encrypt (press Enter twice when finished):")
        
        lines = []
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
        
        content = "\n".join(lines[:-1]) if lines and lines[-1] == "" else "\n".join(lines)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ '{filepath}' created successfully!\n")


def clear_old_files(*filepaths):
    """
    Clear the contents of existing files to avoid interference.
    """
    for filepath in filepaths:
        if os.path.exists(filepath):
            open(filepath, 'w', encoding='utf-8').close()


def get_shift_values():
    """
    Get shift values from user with input validation.
    """
    while True:
        try:
            shift1 = int(input("Enter shift1 (integer): "))
            shift2 = int(input("Enter shift2 (integer): "))
            return shift1, shift2
        except ValueError:
            print(" Please enter valid integers for shift values.")
        except KeyboardInterrupt:
            print("\n Program interrupted by user.")
            exit(0)


def main():
    """
    Main program execution.
    """
    print("Text File Encryption/Decryption Program")
    print("=" * 45)
    
    # File paths
    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    # Check and create raw_text.txt if it doesn't exist
    create_raw_text_file_if_missing(raw_file)

    # Clear old encrypted and decrypted files for cleaner approach
    clear_old_files(encrypted_file, decrypted_file)

    # Get shift values from user
    shift1, shift2 = get_shift_values()
    
    print(f"\n Using shift values: shift1={shift1}, shift2={shift2}")
    print("-" * 45)

    # Perform encryption → decryption → verification
    encrypt_file(raw_file, encrypted_file, shift1, shift2)
    decrypt_file(encrypted_file, decrypted_file, shift1, shift2)
    
    print("-" * 45)
    verify_decryption(raw_file, decrypted_file)
    

    
if __name__ == "__main__":
    main()