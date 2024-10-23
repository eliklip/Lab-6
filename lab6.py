# Elik Lipskar
# Lab 6: Version Control


# Looping menu of options
def looping_menu():
    print('Menu')
    print('-------------')
    print('1. Encode password')
    print('2. Decode password')
    print('3. Exit program\n')


# Returns an encoded password
def encode(password):
    encoded_password = ''

    for num in password:
        if int(num) <= 6:
            encoded_password += (str(int(num) + 3))
        else:
            encoded_password += (str((int(num) + 3) % 10))
    return encoded_password


def decode(encoded_password):
    # EX INPUT = 45678888
    # EX OUT = 12345555
    decoded_password = ''
    for num in encoded_password:
        # handles num [0, 3]
        if int(num) < 3:
            decoded_password += str(int(num) + 7) 
        else:  # handles num [4, 9]
            decoded_password += str(int(num) - 3)
    return decoded_password


def main():
    stored_pass = ''

    while True:
        looping_menu()
        option = int(input('Please enter an option: '))        
        # Needs to call encode function
        if option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!\n')
            stored_pass = ''  # Clears stored pass in case user wants to encode a different password
            stored_pass += encode(password)
        elif option == 2:
            print(f'The encoded password is: {stored_pass}, and the original password is {decode(stored_pass)}.')
        elif option == 3:
            exit()


if __name__ == '__main__':
    main()
