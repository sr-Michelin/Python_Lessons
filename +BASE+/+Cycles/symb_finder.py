while True:
    l = tuple(input('\nВведіть щось нове: '))
    i = (input('Шукаєм: '))

    if l.count(i) != 0:
        print('Даний знак присутній у тексті %s разів(-и)' % (l.count(i)))
    elif '!' in l or '!' in i:
        print('Кінець циклу!')
        break
    else:
        print('Даний знак не зустрічаэться у введеному тексті!\nTry again!')
