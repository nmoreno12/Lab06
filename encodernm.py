#  Nicholas Moreno's Encoder
#  create menu
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')


#  create encoder function
def encode():
    user_pass = str(input('Please enter your password to encode: '))
    encoded_user_pass = ""
    for digit in user_pass:
        encode_digit = str((int(digit) + 3) % 10)
        encoded_user_pass += encode_digit
    print('Your password has been encoded and stored!\n')
    return encoded_user_pass


#  create decoder function


#  create main function with while loop
def main():
    run = True
    while run:
        menu()
        menu_selection = int(input('Please enter an option: '))
        if menu_selection == 1:
            encode()
        if menu_selection == 2:
            pass
        if menu_selection == 3:
            run = False


if __name__ == "__main__":
    main()
