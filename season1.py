import re
import random

def validate_ip(ip):
    segments = ip.split(".")
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit() or not 0 <= int(segment) <= 255:
            return False
    return True

# how to do with regex
# def validate_ip(ip):
#     pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
#     return pattern.match(ip) is not None

#https://es.wikipedia.org/wiki/Direcci%C3%B3n_IP
def get_ip_class(ip):
    if not validate_ip(ip):
        return f"The IP {ip} is invalid"
    
    first_octet = int(ip.split(".")[0])
    if 0 <= first_octet <= 127:
        ip_class = "Class A"
    elif 128 <= first_octet <= 191:
        ip_class = "Class B"
    elif 192 <= first_octet <= 223:
        ip_class = "Class C"
    elif 224 <= first_octet <= 239:
        ip_class = "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        ip_class = "Class E (Experimental)"
    else:
        return f"The ip address {ip} is invalid"

    return f"The ip address {ip} is {ip_class}"

def convert_to_ascii(numero):
    try:
        return chr(numero)
    except ValueError:
        return "Invalid input, please enter a valid integer"

def generate_random_number():
    return random.randint(1, 6)

def concatenate_words(word1, word2):
    return word1 + word2

def menu():
    print("\nSelect an option:\n")
    print("1. Validate ip address (IPv4)")
    print("2. Transform numbers into ASCII code")
    print("3. Generate a random number [1,6]")
    print("4. Concatenate words")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == '5':
            print(";) Happy day from the infrastructure team")
            break
        elif choice == '1':
            ip = input("\tEnter the IP address: ")
            print(f"\t{get_ip_class(ip)}")
        elif choice == '2':
            number = int(input("\tEnter a number: "))
            print(f"\tThe ASCII code is: {convert_to_ascii(number)}")
        elif choice == '3':
            print(f"\tThe random number is: {generate_random_number()}")
        elif choice == '4':
            word1 = input("\tEnter the first word: ")
            word2 = input("\tEnter the second word: ")
            print("\tConcatenated result:", concatenate_words(word1, word2))
        else:
            print("\tInvalid choice, please try again.")

if __name__ == "__main__":
    main()