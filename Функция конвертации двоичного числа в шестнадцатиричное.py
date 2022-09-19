hexadecimal = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4",
                "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9",
                "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E",
                "1111":"F"}


def hex_to_bin(binary):
    """Принимает на вход двоичное число и
    возвращает 16-ричное в формате строки"""

    elements = []
    start = 0
    end = 4
    hex = str()

    binary = str(binary)
    short_zeros = len(binary) // 4

    if short_zeros != 0:
        prefix = "0" * short_zeros
        binary = prefix + binary

    while end <= len(binary):
        key = (binary[start:end])
        start +=4
        end += 4
        hex += hexadecimal[key]

    return (hex)

if __name__ == '__main__':
    print("expectation 3B7")
    print(hex_to_bin(1110110111))
