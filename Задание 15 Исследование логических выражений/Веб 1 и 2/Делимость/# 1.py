"""
Обозначим через ДЕЛ(n, m) утверждение "натуральное число n делится дес остатка на m".
Для какого наименьшего натурального числа А формула бла-бла-бла тождественно истинна"""


def f(x, a):
    # Формула
    return ((x % a == 0) and (x % 36 != 0)) <= (x % 12 != 0)


for a in range(1, 1000):
    # Берём большой диапазон для х. Минимум с десятикратным запасом
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
