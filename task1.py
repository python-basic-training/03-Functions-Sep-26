def sequence(*args):
    pass # def sequence(*args):
    count = len(args)

#0 чисел: возвращаем пустой кортеж
    if count == 0:
        return ()
# 1 число: от 0 до a (или от a до 0), всегда по возрастанию
    elif count == 1:
        a = args[0]
        if a >= 0:
            return tuple(range(0, a + 1))
        else:
            return tuple(range(a, 1))
# передано 2 числа: от 0 до a (или от a до 0), всегда по возрастанию
    elif count == 2:
        a, b = args[0], args[1]
        return tuple(range(min(a, b), max(a, b) + 1))
    else:
        return args


assert sequence(5) == (0, 1, 2, 3, 4, 5), "Ожидался диапазон от 0 до 5"
assert sequence(-3) == (-3, -2, -1, 0), "Ожидался диапазон от -3 до 0"
assert sequence(2, 6) == (2, 3, 4, 5, 6), "Ожидался диапазон от 2 до 6"
assert sequence(10, 7) == (7, 8, 9, 10), "Ожидался диапазон от 7 до 10"
assert sequence(1, 2, 3, 4) == (1, 2, 3, 4), "Ожидался кортеж из переданных чисел"

print("код работает!")


assert sequence(5) == (0, 1, 2, 3, 4, 5), "Ожидался диапазон от 0 до 5"
assert sequence(-3) == (-3, -2, -1, 0), "Ожидался диапазон от -3 до 0"
assert sequence(2, 6) == (2, 3, 4, 5, 6), "Ожидался диапазон от 2 до 6"
assert sequence(10, 7) == (7, 8, 9, 10), "Ожидался диапазон от 7 до 10"
assert sequence(1, 2, 3, 4) == (1, 2, 3, 4), "Ожидался кортеж из переданных чисел"
