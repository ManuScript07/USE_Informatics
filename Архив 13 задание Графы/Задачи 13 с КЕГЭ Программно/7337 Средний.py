"""На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З.
   По каждой дороге можно двигаться только в одном направлении, указанном стрелкой.
   Определите количество различных путей, которые начинаются в городе А и заканчиваются в городе Е
   и проходят через промежуточные города не более одного раза."""

nodes = "АБЗ БВД ВГ ГЖ ДВЕ Е ЖЕД ЗДЕ"
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+c, end) for c in d[s[-1]] if s.count(c) == 0)


print(f('А', 'Е'))

# 7
