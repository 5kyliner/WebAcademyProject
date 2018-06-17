#task07
"""
Дан список строк. Посчитать количество символов в первой строке где есть символ ‘а’.
	[‘‪fur’, ‘skin’, ‘coat’, ‘pelage’, ‘jack‬’] -> 4 # len(‘coat’)
"""
a = ['fur', 'skin', 'coat', 'pelge', 'jack‬']
for i in range(len(a)):
    if ('a' in a[i]) is True:
        print(a[i])
        break

# a = ['fur', 'skin', 'coat', 'pelge', 'jack‬']
# for i in range(len(a)):
#     if a[i].find('a')!=-1:
#         print(a[i])
#         break