def prime (k):
    """Возвращает True,если на вход принято простое число,
    и False в противном случае"""

    if k > 1:
        for i in range(2, int(k/2)+1):
             if (k % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False



if __name__ == '__main__':

    k = int(input("Введите число: "))
    print (prime(k))
