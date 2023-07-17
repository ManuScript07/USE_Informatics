"""На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д. По каждой дороге можно двигаться
   только в одном направлении, указанном стрелкой. Определите количество различных путей ненулевой длины,
   которые начинаются и заканчиваются в городе А, не содержат этот город в качестве промежуточного пункта и проходят
   через промежуточные города не более двух раз."""

nodes = 'АГ БА ВБГ ГВД ДАБВ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+c, end) for c in d[s[-1]] if s.count(c) <= 1)

print(f('Г', 'А'))

# 12
