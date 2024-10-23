# Elik Lipskar
# Lab 6: Version Control


def looping_menu():
    print('Options Menu')
    print('------------')
    print('1. Encode password')
    print('2. Decode password')
    print('3. Exit program\n')


def user_selection(option):
    if option == 1:
        password = input('Please input your password for encryption: ')
        print('Your password has been encoded.')
        return encode(password)
    elif option == 2:
        pass
    # FIXME!! PLEASE CREATE A DECODE FUNCTION
    elif option == 3:
        exit()


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
        option = int(input('Please select an option: '))
        user_selection(option)
        print()


if __name__ == '__main__':
    main()
