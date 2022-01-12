def l_sort(list_):
    list_.sort()
    return list_


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2
    if array[middle] == element:
        idx = middle
        while idx > 0:
            if array[idx - 1] < array[middle]:
                break
            idx -= 1
        if idx - 1 >= 0:
            return f'Индекс меньшего числа = "{idx - 1}"'
        else:
            return f"Элемента меньшего {element} нет в списке"

    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


array = ""
element = None
while not isinstance(array, list):
    array = input("Введите числа через пробел ")
    element = int(input("Введите любое число "))
    try:
        array = list(map(int, array.split()))
    except ValueError as e:
        print("Неверный ввод")

array.append(element)  # На случай поиска относительно числа, которого нет в списке
array = l_sort(array)
left = 0
right = len(array) - 1

if element <= array[0]:
    print("Ошибка. Введенное число не может быть меньше либо равным наименьшему в списке.")
elif element >= array[-1]:
    print("Ошибка. Введенное число не может быть больше либо равным наибольшему в списке.")
else:
    print(binary_search(array, element, left, right))







