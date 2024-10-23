# Elik Lipskar
# Lab 6: Version Control


def looping_menu():
    print('Menu')
    print('-------------')
    print('1. Encode password')
    print('2. Decode password')
    print('3. Exit program\n')


def encode(password):
    encoded_password = ''

    for num in password:
        if int(num) <= 6:
            encoded_password += (str(int(num) + 3))
        else:
            encoded_password += (str((int(num) + 3) % 10))
    return encoded_password


def main():
    while True:
        looping_menu()
        option = int(input('Please enter an option: '))
        stored_pass = ''

        if option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            stored_pass += password
        elif option == 2:
            pass
            # FIXME!! PLEASE CREATE A DECODE FUNCTION
        elif option == 3:
            exit()
        print()


if __name__ == '__main__':
    main()
