import logging

file = open('lorum.txt', 'w')
file.write('NewHello')
file.close()

lst = []
for i in range(100):
    file = open('lorum.txt', 'w')
    lst.append(file)
    file.close()

with open('lorum.txt', 'w') as f:
    f.write('123')
    f.write('hello')
print('end')

# Не каждая функция поддерживает менеджер контеста
logging.basicConfig(filename='part3.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
try:
    with print('lorum.txt', 'w') as f:
        f.write('123')
        f.write(123)
    print('end')
except Exception as e:
    logging.error(f'Ошибка при записи в файл: {e}')




