def bubble_sort(list):
    """Сравнивает текущий элемент списка со следующим.
    Если следующий элемент больше текущего, меняет их местами.
    Если массив отсортирован, заканчивает работу."""

    operating_range = len(list) - 1
    i = 0
    a = 0
    while a <= operating_range:
        for i in range (1,len(list)):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
        a = a + 1
    operating_range = operating_range - 1


if __name__ == '__main__':
    #Заранее сгенерированный рандомный список:
    list = [82, 69, 18, 46, 40, 98, 74, 41, 13, 0,
            36, 39, 10, 79, 95, 87, 48, 4, 15, 89]

    print(list)
    bubble_sort(list)
    print("Сортировка выполнена. Полученный результат:")
    print(list)
