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
