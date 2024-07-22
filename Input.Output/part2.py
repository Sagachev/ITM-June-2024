file = open('lorum.txt', 'r+')  # 'r+' открывает для чтения и записи,  добавляет запись в начало файла
file.write('Hello')

file = open('lorum.txt', 'w')  # 'w' открывает записи, удаляет предыдущую запись
file.write('Hello')

file = open('lorum.txt', 'a')  # 'а' открывает для чтения и записи, добавляет запись в конец файла
file.write('Hellomoto')

