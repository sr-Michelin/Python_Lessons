with open('py.txt','r') as f:
    for line in f:
        print()

running = True
num = int(line)
while running:
    try:
         num_predicted = int(input('\nВведіть число: '))
         if num_predicted > num:
             print('Введене число більше шуканого')
         elif num_predicted < num:
             print('Введене число менше шуканого')
         else:
             print('Вгадали!')
             running = False
    except ValueError:
        print("Ви ввели не число! \nTry again!")