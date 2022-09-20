def hex_to_bin(binary,reverse = False):
    """Принимает на вход двоичное число и возвращает 16-ричное
    в формате строки. Может принимать 16-ричное число и возвращать
    двоичное при втором параметре reverse = True"""

    hexadecimal = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4",
                    "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9",
                    "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E",
                    "1111":"F"}

    elements = []
    start = 0
    end = 4
    hex = str()
    binary = str(binary)
    short_zeros = len(binary) // 4
    step = 4

    if short_zeros != 0 and reverse == False:
        prefix = "0" * short_zeros
        binary = prefix + binary

    if reverse:
        rev_hex = {}
        step = 1
        end = 1
        for key, value in hexadecimal.items():
            rev_hex[value] = key

    while end <= len(binary):
        key = (binary[start:end])
        start += step
        end += step
        if not reverse:
            hex += hexadecimal[key]
        else: 
            hex += rev_hex[key]

    return (hex)


if __name__ == '__main__':
    print("expectation 3B7")
    print(hex_to_bin(1110110111))
    print("expectation 101001001011")
    print(hex_to_bin('A4B', reverse=True))
