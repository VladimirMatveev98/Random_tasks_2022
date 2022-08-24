def sec_conv(seconds):
    sec = seconds % 60
    min = seconds // 60
    hours = min // 60
    min = min % 60
    days = hours // 24
    hours = hours % 24

    return (days, hours, min, sec)


if __name__ == '__main__':

    print("expectation 5, 18, 53, 20\n")
    print(sec_conv(500000))
