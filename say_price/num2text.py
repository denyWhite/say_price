# -*- coding: utf-8 -*-
"""
:authors: Denis Belov
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2019 Denis Belov
"""

import decimal

units = (
    'ноль',
    ('один', 'одна'),
    ('два', 'две'),
    'три', 'четыре', 'пять',
    'шесть', 'семь', 'восемь', 'девять'
)

teens = (
    'десять', 'одиннадцать',
    'двенадцать', 'тринадцать',
    'четырнадцать', 'пятнадцать',
    'шестнадцать', 'семнадцать',
    'восемнадцать', 'девятнадцать'
)

tens = (
    teens,
    'двадцать', 'тридцать',
    'сорок', 'пятьдесят',
    'шестьдесят', 'семьдесят',
    'восемьдесят', 'девяносто'
)

hundreds = (
    'сто', 'двести',
    'триста', 'четыреста',
    'пятьсот', 'шестьсот',
    'семьсот', 'восемьсот',
    'девятьсот'
)

orders = (
    (('тысяча', 'тысячи', 'тысяч'), 'f'),
    (('миллион', 'миллиона', 'миллионов'), 'm'),
    (('миллиард', 'миллиарда', 'миллиардов'), 'm'),
)

minus = 'минус'


def thousand(rest, sex):
    prev = 0
    plural = 2
    name = []
    use_teens = 19 >= rest % 100 >= 10
    if not use_teens:
        data = ((units, 10), (tens, 100), (hundreds, 1000))
    else:
        data = ((teens, 10), (hundreds, 1000))
    for names, x in data:
        cur = int(((rest - prev) % x) * 10 / x)
        prev = rest % x
        if x == 10 and use_teens:
            plural = 2
            name.append(teens[cur])
        elif cur == 0:
            continue
        elif x == 10:
            name_ = names[cur]
            if isinstance(name_, tuple):
                name_ = name_[0 if sex == 'm' else 1]
            name.append(name_)
            if 4 >= cur >= 2:
                plural = 1
            elif cur == 1:
                plural = 0
            else:
                plural = 2
        else:
            name.append(names[cur-1])
    return plural, name


def num2text(num, main_units=(('', '', ''), 'm')):
    _orders = (main_units,) + orders
    if num == 0:
        return ' '.join((units[0], _orders[0][0][2])).strip() # ноль

    rest = abs(num)
    ord = 0
    name = []
    while rest > 0:
        plural, nme = thousand(rest % 1000, _orders[ord][1])
        if nme or ord == 0:
            name.append(_orders[ord][0][plural])
        name += nme
        rest = int(rest / 1000)
        ord += 1
    if num < 0:
        name.append(minus)
    name.reverse()
    return ' '.join(name).strip()


def decimal2text(value, places=2,
                 int_units=(('', '', ''), 'm'),
                 exp_units=(('', '', ''), 'm')):
    value = decimal.Decimal(value)
    q = decimal.Decimal(10) ** -places
    integral, exp = str(value.quantize(q)).split('.')
    return u'{} {}'.format(
        num2text(int(integral), int_units),
        num2text(int(exp), exp_units))

