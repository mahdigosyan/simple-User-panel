from datetime import datetime


def Outp():
    infile = open('output.txt', 'a+', encoding="utf-8")
    admin = open('users.txt', 'r+', encoding='utf-8')
    i = input('\nEnter your username and password separated by a space: ').split()
    if len(i) > 1:
        for line in admin:
            f = line.split()
            if i[0] == f[0] and i[1] == f[1]:
                infile.write(
                    'User' + ' ' + f[0] + ' successfully logged in' + ' ' + str(datetime.today())[:19] + '\n')
                i[1] = True
                if f[2] == 'True':
                    i.append('True')
                else:
                    i.append('False')
                print(i)
                break

    elif len(i) != 2:
        infile.write('The username or password you entered is incorrect:' + ' ' + i[0] + ' ' + str(datetime.today())[:19] + '\n')
        i = ['guest', False, 'False']
    admin.close()
    infile.close()
    return i


def Cnk():
    user = Outp()
    if 'admin' in user[0] and user[1] == True:
        print('Hello user:' + user[0], '\n', '1)View log file', '\n',
              '2)View list of users', '\n', '3)Change the Users password \n',
              '4)Add user \n', '5)Delete user \n', '6)Block user\n',
              '7)Unblock user\n', '8)Exit\n')
        i = int(input())
        while i != 8:
            if i == 1:
                print('//-------------------------------------\\' + '\\')
                [print(i, end='') for i in open('output.txt', encoding='utf-8')]
                print('//_____________________________________\\' + '\\')
                open('output.txt', 'a+', encoding='utf-8').write(
                    'The administrator looked at the logs' + ' ' + str(datetime.today())[:19] + '\n')

            elif i == 2:
                print('*----------------------------*')
                [print(i, end='') for i in open('users.txt', encoding='utf-8')]
                print('\n*____________________________*')
                open('output.txt', 'a+', encoding='utf-8').write(
                    'The administrator looked at the list of users' + ' ' + str(datetime.today())[:19] + '\n')

            elif i == 3:
                us = input('Enter your username: ')
                cache = open('users.txt', 'r', encoding='utf-8').read().split()
                open('users.txt', 'w').close()  # clear file
                for i in range(len(cache)):  # search on target word
                    if cache[i] == us:
                        passw = input(
                            'The password must contain numbers, Latin and digits.\n' + 'Enter the password you want to change: ')
                        if mask(passw):
                            cache[i + 1] = passw
                            open('output.txt', 'a+', encoding='utf-8').write(
                                'Users password' + us + ' successfully changed' + ' ' + str(datetime.today())[
                                                                                           :19] + '\n')

                            break
                        else:
                            print('The password does not match the requirements\n')
                            open('output.txt', 'a+', encoding='utf-8').write(
                                'Failed to change user password' + us + ' ' + str(datetime.today())[
                                                                                          :19] + '\n')
                            break
                f = open('users.txt', 'w', encoding='utf-8')
                for i in range(0, len(cache), 3):  # write in file from the cache
                    f.write(cache[i] + ' ' + cache[i + 1] + ' ' + cache[i + 2] + '\n')

                f.close()

            elif i == 4:
                name = input('Enter login: ')
                passw = input(
                    'enter password\nThe password must contain number, Latin, numbers and be more than 7 characters long\n')
                if mask(passw):
                    open('users.txt', 'a+', encoding="utf-8").write(name +
                                                                    ' ' + passw + ' ' + 'True' + '\n')
                    open('output.txt', 'a+', encoding='utf-8').write(
                        'User ' + name + ' successfully added' + ' ' + str(datetime.today())[:19] + '\n')
                else:
                    print('Password is not allowed.\nReturn to menu')
                    open('output.txt', 'a+', encoding='utf-8').write(
                        'User ' + name + ' not added' + ' ' + str(datetime.today())[:19] + '\n')

            elif i == 5:
                us = input('Enter your username: ')
                cache = open('users.txt', 'r', encoding='utf-8').read().split()
                open('users.txt', 'w').close()  # clear file
                for i in range(len(cache)):  # search on target word
                    if cache[i] == us:
                        del cache[i]
                        del cache[i]
                        del cache[i]
