import ClassMenu
import ClassTool

LoopStatus = True
OprationInput = 0
RegisterStatus = False

FullName = ''
Email = ''
Username = ''
Password = ''

FullNames = ['Ali Mohammadi']
Emails = ['alimohammadi.dev@gmail.com']
Usernames = ['alimo_dev']
Passwords = ['@123']

while LoopStatus:

    ClassMenu.menu.Main('self')
    OprationInput = int(input('Enter an option: '))

    if OprationInput == 1:

        print('test')

    elif OprationInput == 2:
        FullName = input('Enter Full Name: ')
        Email = input('Enter Email: ').lower()
        Username = input('Enter Username: ').lower()
        Password = input('Enter Password: ').upper()

        print()

        ClassMenu.menu.Register('self')
        OprationInput = int(input('Enter an option: '))

        if OprationInput == 1:
            RegisterStatus =  ClassTool.tool.ToExist('self',Usernames,Username)
            if RegisterStatus == False:
                FullNames.append(FullName)
                Emails.append(Email)
                Usernames.append(Username)
                Passwords.append(Password)
            else:
                print('Error')


    elif OprationInput == 3:
        print('test')
    else:
        print('Input Invalid!')