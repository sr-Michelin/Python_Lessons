name = 'Mike'

if name.startswith('M'):  # Перевірка на початок строки з шуканого символа
    print('"M" in "Mike"!')

if 'i' in name:
    print('"i" in "Mike"!')

if name.find('ke') != -1:  # find возвращает -1,если подстрока не обнаружена
    print('"ke" in "Mike"!')

delimiter = '_*_'
country_list = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(country_list))  # Розділення через "join"
