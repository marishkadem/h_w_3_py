"""Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов."""

old_list = [1, 2, 1, 5, 2, 7, 9, 0, 0, 1]
uni_list = []
double_list = []

for item in old_list:
    if item in uni_list:
        if item in double_list:
            pass
        else:
            double_list.append(item)
    else:
        uni_list.append(item)

print(double_list)
print(uni_list)