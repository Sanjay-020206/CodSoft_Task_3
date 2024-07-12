import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    length_input = input("Enter the desired length of the password: ")
    
    if length_input.isdigit():
        length = int(length_input)
        if length > 0:
            password = generate_password(length)
            print(f"Generated password of length {length}:")
            print(password)
        else:
            print("Password length must be greater than zero.")
    else:
        print("Invalid input. Please enter a valid integer for the password length.")
if __name__ == "__main__":
    main()
