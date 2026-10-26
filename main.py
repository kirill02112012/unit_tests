def check_name(name):
    if any(char.isdigit() for char in name) or not name.replace(" ", "").isalpha():
        return False
    else:
        return True


def division(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Можно подставлять только целые числа!!!')
    if b == 0:
        raise ZeroDivisionError('Нельзя делить на ноль!!!')

    return a/b


def check_phone(phone: str) -> bool:
    # Номер должен содержать ровно 11 символов
    if len(phone) != 11:
        return False

    # Первый символ должен быть "7" или "8"
    if phone[0] not in ("7", "8"):
        return False

    # Все остальные символы должны быть цифрами
    for i in range(1, len(phone)):
        if not phone[i].isdigit():
            return False

    return True

print(check_phone("76491234567"))