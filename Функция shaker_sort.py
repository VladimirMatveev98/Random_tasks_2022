def shaker_sort(list):
    """Проходит по массиву, сравнивая текущий элемент со следующим. Если
    следующий элемент меньше, меняет их местами. Пройдя до конца, начинает
    сравнивать текщий элемент с предыдущим. Если предыдущий элемент больше,
    меняет их местами."""

    i = 0
    a = 0
    operating_range = len(list) - 1
    while a <= operating_range:
        for i in range (1,operating_range):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
        i = 0
        for i in range (operating_range,1, -1):
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
        a = a + 2
        operating_range = operating_range - 1


if __name__ == '__main__':


    list = [73, 87, 5, 34, 70, 54, 35, 59, 99, 74, 29, 1, 62,
        65, 44, 25, 80, 8, 9, 16]

    print(list)
    shaker_sort(list)
    print("Сортировка выполнена. Полученный результат:")
    print(list)
