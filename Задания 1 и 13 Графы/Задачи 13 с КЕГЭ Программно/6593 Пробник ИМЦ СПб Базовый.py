"""На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К, Л, М, Н.
   По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. Определите
   количество различных путей ненулевой длины, которые начинаются и заканчиваются в городе Е, не содержат
   этот город в качестве промежуточного пункта и проходят через промежуточные города не более одного раза.
"""

nodes = 'АБГ БЕ ВА ГЕЖ ДБЕ ЕИКВ ЖЕ ЗДЕ ИМ КЖМН ЛЗ МЛЗ НМ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s + c, end) for c in d[s[-1]] if s.count(c) == 0)


print(f('И', 'Е') + f('К', 'Е') + f('В', 'Е'))

# 22
