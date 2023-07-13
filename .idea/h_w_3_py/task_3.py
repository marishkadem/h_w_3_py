"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один
допустимый вариант."""

weight = int(input('Введите грузоподъемность рюкзака в кг: '))
items_dict = {'вода': 4, 'нож': 0.5, 'палатка': 5, 'кружка': 1, 'тарелка': 1, 'консервы': 3, 'фонарик': 0.5,
              'спички': 0.1, 'книга': 1,}
res_list = []
items_dict = dict(sorted(items_dict.items(), key=lambda item: item[1]))

for item in items_dict:
    if items_dict[item] < weight:
        res_list.append(item)
        weight -= items_dict[item]

print(res_list)