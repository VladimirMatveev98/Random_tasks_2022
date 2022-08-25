def conv_binary(denary):
    """Принимает целое десятичное число и возвращает его же,
    записанное в двоичном виде. ВАЖНО: Для корректной записи в
    двоичном коде используется формат строки."""
    
    binary_interim = int()
    binary = str()

    while denary > 0:

        binary_interim = denary % 2 #Проверка на чётность,получение 0 или 1
        binary_interim = str(binary_interim) #Подготовка к сложению строк
        binary = binary + binary_interim #Добавление к числу 0 или 1
        denary = denary // 2 #Деление на 2 без учёта дробных частей

    binary = (binary)[::-1]  #Реверс переменной для корректной записи
    return binary



if __name__ == '__main__':
    print("expectation 1100100")
    print(conv_binary(100))
    denary = int(input("\nВведите десятичное число для\n\
конвертации в двоичную систему счисления:"))
    print(conv_binary(denary))
