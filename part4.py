# Используя операции индексирования и среза выведите на экран первый и третий элементы списка [1, 2, 3 ,4 ,5], а также срез списка из первых трех элементов.
l = [1, 2, 3 ,4 ,5]
print(l[0], l[2], l[:3], sep='\n')

# Дан список [«Ростов», «+», «на», «-», «Дону»]. Исправьте плюс на дефис и выведите название города на экран использовав доступ к элементам списка по индексам
l = ['Ростов', '+', 'на', '-', 'Дону']
l[1] = '-'
print(l[0], l[1], l[2], l[3], l[4])

# Дан список [«a», «s», «1», «a», «32», «23»]. Разбейте его на два списка: только с буквами и только с числами. 
l = ["a", "s", "1", "a", "32", "23"]
letters = [x for x in l if x.isalpha()]
numbers = [x for x in l if x.isdigit()]
print(letters, numbers, sep='\n')

# В предыдущей задаче должен был получиться список из букв. Используя методы списков: удалите из него последний элемент, сделайте реверсию списка.
l = ['a', 's', 'a']
del l[-1]
l.reverse()
print(l)

# Преобразуйте список [«a», «s», «1», «a», «32», «23»] в set и выведите на экран. Что изменилось?
l = ['a', 's', '1', 'a', '32', '23']
set = set(l)
print(set)
#удаляются дубликаты списка, очередность заполнения может меняться