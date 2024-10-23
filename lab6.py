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


# FIXME!!! NEEDS A DECODE() FUNCTION HERE
def main():
    while True:
        looping_menu()
        option = int(input('Please enter an option: '))
        stored_pass = ''  # Out of if-elif branches, so it can be used for decode function

        if option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!\n')
            stored_pass = ''  # Clears stored pass in case user wants to encode a different password
            stored_pass += password
        elif option == 2:
            pass
            # FIXME!! PLEASE REFER TO DECODE FUNCTION
        elif option == 3:
            exit()


if __name__ == '__main__':
    main()
