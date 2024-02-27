"""ZeroDivisionError"""
first_num = int(input("Enter the number: "))
second_num = int(input("Enter the number: "))


def div_zero(a, b):
    """ZeroDivisionError"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot be divided by ZERO")
        return None


print(div_zero(first_num, second_num))
