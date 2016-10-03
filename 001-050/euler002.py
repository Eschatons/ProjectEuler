# -*- coding: utf-8 -*-

''' even fibbonaci numbers '''
from eulerHelpers import fibbonaci_under

even_fibs = (x for x in fibbonaci_under(4 * (10 ** 6)) if x % 2 == 0)
print(sum(even_fibs))
