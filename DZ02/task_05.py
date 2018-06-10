#task 05
"""
Напишите программу, запрашивающую имя, фамилия, отчество и номер группы студента и выводящую введённые данные в следующем виде:
 ************************************
 *Лабораторная работа № 1   *
 *Выполнил(а): ст. гр. ЗИ-123 *
 *Иванов Андрей Петрович    *
 ************************************
"""
# a = str(input("Pls enter student's 1stname\n>"))
# b = str(input("Pls enter student's 2stname\n>"))
# c = str(input("Pls enter student's patronymic\n>"))
# d = str(input("Pls enter student's group No.\n>"))
a = 'Bw'
b = 'sdwer'
c = 'sw'
d = 'DN3221'
string = ['Лабораторная работа N 1', 'Выполнил(а): ст. гр.' + d, "{} {} {}".format(a, b, c)]

def find_max(string):
    strs = string[0]
    for strs_max in string:
        if int(len(strs)) < int(len(strs_max)):
            strs = strs_max
    return strs
find_max(string)

w = int(len(find_max(string))) + 2

print ('*' * (w + 2))
cstr = "*{:^%s}*" % w
print(cstr.format(string[0]))
print(cstr.format(string[1]))
print(cstr.format(string[2]))
print ('*' * (w + 2))